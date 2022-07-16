from flask import request, render_template, url_for, redirect, flash
from . import db
from . import models, forms
from flask_login import login_user, logout_user, login_required, current_user

# post functions

def index():
    customers = models.Customer.query.all()
    return render_template('index.html', customers=customers)

@login_required
def customer_create():
    form = forms.CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_customer = models.Customer(name=request.form.get('name'),
                                   phone_number=request.form.get('phone_number'),
                                   item=request.form.get('item'),
                                   quantity=request.form.get('quantity'),
                                   price=request.form.get('price'),
                                   user_id=current_user.id)
            db.session.add(new_customer)
            db.session.commit()
            flash('Клиент успешно добавлен', category='success')
            return redirect(url_for('index'))
        if form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category='danger')

    return render_template('customer_create.html', form=form)


def customer_detail(customer_id):
    customer = models.Customer.query.get(customer_id)
    return render_template('customer_detail.html', customer=customer)


@login_required
def customer_delete(customer_id):
    customer = models.Customer.query.get(customer_id)
    if customer:
        form = forms.CustomerForm(obj=customer)
        if customer.user_id == current_user.id:
            if request.method == 'POST':
                db.session.delete(customer)
                db.session.commit()
                flash('клиент удален', category='success')
                return redirect(url_for('index'))
            else:
                return render_template('customer_delete.html', customer=customer, form=form)
        else:
            flash('У вас нет прав для удаления записи', category='danger')
            return redirect(url_for('index'))
    else:
        flash('клиент не найден', category='danger')
        return redirect(url_for('index'))


@login_required
def customer_update(customer_id):
    customer = models.Customer.query.filter_by(id=customer_id).first()
    if customer:
        if customer.user_id == current_user.id:
            form = forms.CustomerForm(obj=customer)
            if request.method == 'POST':
                if form.validate_on_submit():
                    customer.name = request.form.get('name')
                    customer.phone_number = request.form.get('phone_number')
                    customer.item = request.form.get('item')
                    customer.quantity = request.form.get('quantity')
                    customer.price = request.form.get('price')
                    db.session.commit()
                    flash('Данные клиента успешно обновлены', category='success')
                    return redirect(url_for('index'))
                if form.errors:
                    for errors in form.errors.values():
                        for error in errors:
                            flash(error, category='danger')
            return render_template('customer_update.html', customer=customer, form=form)
        else:
            flash('у вас недостаточно прав', category='danger')
            return redirect(url_for('index'))
    else:
        flash('клиент не найден', category='danger')
        return redirect(url_for('index'))


# user functions

def register():
    form = forms.UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = models.User(username=request.form.get('username'), password=request.form.get('password'))
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно зарегистрированы', category='success')
            return redirect(url_for('login'))

        elif form.errors:
            for errors in form.errors.values:
                for error in errors:
                    flash(error, category='danger')
    return render_template('register.html', form=form)


def login():
    form = forms.UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = models.User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                flash('Вы успешно вошли в систему', category='success')
                return redirect(url_for('index'))
            else:
                flash('Неверный логин или пароль', category='danger')
                return render_template('login.html', form=form)
        if form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category='danger')
    return render_template('login.html', form=form)


def logout():
    logout_user()
    flash('Вы вышли из системы', category='success')
    return redirect(url_for('login'))