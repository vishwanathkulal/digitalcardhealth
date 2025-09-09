from flask import Flask, render_template, request, url_for
import os
import qrcode
import psycopg2
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['QR_FOLDER'] = 'static/qr'
app.config['DOC_FOLDER'] = 'static/documents'

# Render PostgreSQL URL (Replace with your real one if different)
DATABASE_URL = "postgresql://card_db_zwpm_user:BaVxR7VSS3MbTEnI5UyVsh059YsA150p@dpg-d1tudt2dbo4c73e14rd0-a.oregon-postgres.render.com/card_db_zwpm"

# Create folders if not exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['QR_FOLDER'], exist_ok=True)
os.makedirs(app.config['DOC_FOLDER'], exist_ok=True)

def get_db():
    return psycopg2.connect(DATABASE_URL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    form = request.form.to_dict()
    card_id = form.get('card_id')

    # Upload photo
    photo = request.files.get('photo')
    photo_filename = ''
    if photo and photo.filename:
        photo_filename = f"{card_id}_{secure_filename(photo.filename)}"
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

   
    docs = []
    for i in range(1, 4):
        doc = request.files.get(f'document{i}')
        if doc and doc.filename:
            doc_filename = f"{card_id}_doc{i}_{secure_filename(doc.filename)}"
            doc.save(os.path.join(app.config['DOC_FOLDER'], doc_filename))
            docs.append(doc_filename)
        else:
            docs.append('')


    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute('''
            INSERT INTO cards (
                card_id, name, dob, gender, phone, address, blood_group,
                disabilities, allergies, conditions, vaccinations,
                issue_date, doctor, access_code,
                emergency_name1, emergency_phone1, relation1,
                emergency_name2, emergency_phone2, relation2,
                photo, doc1, doc2, doc3
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (card_id) DO NOTHING;
        ''', (
            card_id,
            form.get('name'), form.get('dob'), form.get('gender'), form.get('phone'),
            form.get('address'), form.get('blood_group'), form.get('disabilities'),
            form.get('allergies'), form.get('conditions'), form.get('vaccinations'),
            form.get('issue_date'), form.get('doctor'), form.get('access_code'),
            form.get('emergency_name1'), form.get('emergency_phone1'), form.get('relation1'),
            form.get('emergency_name2'), form.get('emergency_phone2'), form.get('relation2'),
            photo_filename, docs[0], docs[1], docs[2]
        ))
        conn.commit()
    except Exception as e:
        print(f"Database Error: {e}")
        return "An error occurred while saving the data.", 500
    finally:
        cur.close()
        conn.close()

   
    view_url = url_for('view_card', card_id=card_id, _external=True)
    qr_filename = f"{card_id}.png"
    qr_path = os.path.join(app.config['QR_FOLDER'], qr_filename)
    qrcode.make(view_url).save(qr_path)

    return render_template('result.html', qr_filename=qr_filename, card_id=card_id)

@app.route('/view/<card_id>')
def view_card(card_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM cards WHERE card_id = %s', (card_id,))
    row = cur.fetchone()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    if not row:
        return "Health card not found", 404

    data = dict(zip(colnames, row))
    qr_path = url_for('static', filename=f'qr/{card_id}.png')

    documents = []
    for doc_field in ['doc1', 'doc2', 'doc3']:
        if data.get(doc_field):
            documents.append(url_for('static', filename=f'documents/{data[doc_field]}'))

    return render_template('viewcard.html', data=data, qr_path=qr_path, documents=documents)

@app.route('/download_card/<card_id>')
def download_card(card_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM cards WHERE card_id = %s', (card_id,))
    row = cur.fetchone()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    if not row:
        return "Health card not found", 404

    data = dict(zip(colnames, row))
    qr_path = url_for('static', filename=f'qr/{card_id}.png')

    return render_template('healthcard.html', data=data, qr_path=qr_path)

if __name__ == '__main__':
    app.run(debug=True)
