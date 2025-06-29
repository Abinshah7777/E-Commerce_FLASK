from flask import Flask, render_template, request, redirect, flash, url_for
from service.catalogue_service import CatalogueService
from dto.catalogue_dto import Catalogue
from exceptions.exceptions import CatalogueNotFoundError, InvalidCatalogueInputError

app = Flask(__name__)
app.secret_key = 'your_secret_key' 
service = CatalogueService()

@app.route('/')
def index():
    catalogues = service.get_all_catalogues()
    return render_template('index.html', catalogues=catalogues)

@app.route('/create', methods=['GET', 'POST'])
def create_catalogue():
    if request.method == 'POST':
        try:
            data = request.form
            catalogue = Catalogue(
                int(data['catalogue_id']),
                data['catalogue_name'],
                data['catalogue_version'],
                bool(int(data['is_cat_active'])),
                data['catalogue_start'],
                data['catalogue_end']
            )
            service.create_catalogue(catalogue)
            flash('Catalogue created successfully!')
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e))
    return render_template('form.html', action="Create")

@app.route('/update/<int:catalogue_id>', methods=['GET', 'POST'])
def update_catalogue(catalogue_id):
    catalogue = service.get_catalogue_by_id(catalogue_id)
    if not catalogue:
        flash(f"Catalogue ID {catalogue_id} not found.")
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            data = request.form
            updated_catalogue = Catalogue(
                catalogue_id,
                data['catalogue_name'],
                data['catalogue_version'],
                bool(int(data['is_cat_active'])),
                data['catalogue_start'],
                data['catalogue_end']
            )
            service.update_catalogue_by_id(catalogue_id, updated_catalogue)
            flash(f"Catalogue ID {catalogue_id} updated successfully!")
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e))

    return render_template('form.html', action="Update", catalogue=catalogue)

@app.route('/view/<int:catalogue_id>')
def view_catalogue(catalogue_id):
    catalogue = service.get_catalogue_by_id(catalogue_id)
    if catalogue:
        return render_template('view.html', catalogue=catalogue)
    flash(f"Catalogue ID {catalogue_id} not found.")
    return redirect(url_for('index'))

@app.route('/delete/<int:catalogue_id>')
def delete_catalogue(catalogue_id):
    try:
        service.delete_catalogue_by_id(catalogue_id)
        flash(f"Deleted catalogue ID {catalogue_id}")
    except Exception as e:
        flash(str(e))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
