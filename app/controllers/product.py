from flask import Blueprint, flash, request, render_template, redirect, url_for
from app.models.product import Product
from app import db

# A Blueprint groups related routes under one name
product_bp = Blueprint('product', __name__)

# Route: show all students
@product_bp.route('/')
def list_products():
    products = Product.query.all()  # Ask Model for all records
    return render_template('product/list.html', products=products)

# Route: show one student by ID
@product_bp.route('/product/<int:product_id>')
def student_detail(product_id):
    product = Product.query.get(product_id)  # Ask Model for one record
    return render_template('product/detail.html', product=product)

# — CREATE ——————————————————————————————————————————————————————————
@product_bp.route('/product/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name   = request.form.get('name')
        price = request.form.get('price')
        type  = request.form.get('type')

        # Validate — make sure no field is empty
        if not name or not price or not type:
            flash('All fields are required.', 'error')
            return redirect(url_for('product.create_product'))

        # Create the new Student object and save it
        new_product = Product(name=name, price=price, type=type)
        db.session.add(new_product)
        db.session.commit()

        flash('Product added successfully!', 'success')
        return redirect(url_for('product.list_products'))

    # GET request — show the empty form
    return render_template('product/create.html')

# — UPDATE ——————————————————————————————————————————————————————————
@product_bp.route('/product/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get(product_id)

    if product is None:
        flash('Product not found.', 'error')
        return redirect(url_for('product.list_products'))

    if request.method == 'POST':
        name   = request.form.get('name')
        price = request.form.get('price')
        type  = request.form.get('type')

        # Validate
        if not name or not price or not type:
            flash('All fields are required.', 'error')
            return redirect(url_for('product.edit_product', product_id=product_id))

        # Update the existing record's attributes
        product.name   = name
        product.price = price
        product.type  = type
        db.session.commit()

        flash('Product updated successfully!', 'success')
        return redirect(url_for('product.list_products'))

    # GET — show the pre-filled edit form
    return render_template('product/edit.html', product=product)

# — DELETE ——————————————————————————————————————————————————————————
@product_bp.route('/product/<int:product_id>/delete', methods=['GET', 'POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)

    if product is None:
        flash('Product not found.', 'error')
        return redirect(url_for('product.list_products'))

    if request.method == 'POST':
        db.session.delete(product)
        db.session.commit()

        flash(f'{product.name} has been deleted.', 'success')
        return redirect(url_for('product.list_products'))

    # GET — show the confirmation page
    return render_template('product/confirm_delete.html', product=product)