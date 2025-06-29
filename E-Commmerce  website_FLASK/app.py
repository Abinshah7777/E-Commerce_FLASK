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
                catalogue_id=int(data['catalogue_id']),
                catalogue_name=data['catalogue_name'],
                catalogue_version=data['catalogue_version'],
                is_cat_active=bool(int(data['is_cat_active'])),
                catalogue_start=data['catalogue_start'],
                catalogue_end=data['catalogue_end']
            )
            service.create_catalogue(catalogue)
            flash('Catalogue created successfully!', 'success')
            return redirect(url_for('index'))
        except (InvalidCatalogueInputError, ValueError) as e:
            flash(str(e), 'error')
        except Exception as e:
            flash(f"Unexpected error: {str(e)}", 'error')

    return render_template('form.html', action="Create")


@app.route('/update/<int:catalogue_id>', methods=['GET', 'POST'])
def update_catalogue(catalogue_id):
    try:
        catalogue = service.get_catalogue_by_id(catalogue_id)
    except CatalogueNotFoundError as e:
        flash(str(e), 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            data = request.form
            updated_catalogue = Catalogue(
                catalogue_id=catalogue_id,
                catalogue_name=data['catalogue_name'],
                catalogue_version=data['catalogue_version'],
                is_cat_active=bool(int(data['is_cat_active'])),
                catalogue_start=data['catalogue_start'],
                catalogue_end=data['catalogue_end']
            )
            service.update_catalogue_by_id(catalogue_id, updated_catalogue)
            flash(f"Catalogue ID {catalogue_id} updated successfully!", 'success')
            return redirect(url_for('index'))
        except (InvalidCatalogueInputError, ValueError) as e:
            flash(str(e), 'error')
        except Exception as e:
            flash(f"Unexpected error: {str(e)}", 'error')

    return render_template('form.html', action="Update", catalogue=catalogue)


@app.route('/view/<int:catalogue_id>')
def view_catalogue(catalogue_id):
    try:
        catalogue = service.get_catalogue_by_id(catalogue_id)
        return render_template('view.html', catalogue=catalogue)
    except CatalogueNotFoundError as e:
        flash(str(e), 'error')
        return redirect(url_for('index'))


@app.route('/delete/<int:catalogue_id>')
def delete_catalogue(catalogue_id):
    try:
        service.delete_catalogue_by_id(catalogue_id)
        flash(f"Deleted catalogue ID {catalogue_id}", 'success')
    except CatalogueNotFoundError as e:
        flash(str(e), 'error')
    except Exception as e:
        flash(f"Unexpected error: {str(e)}", 'error')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
