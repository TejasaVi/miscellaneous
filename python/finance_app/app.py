from flask import Flask, flash, render_template, request, redirect, url_for, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Flash messages require a secret key
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            return render_template('signup.html', error='Username already exists')
        
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    response = redirect(url_for('login'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response

# Models
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(100), nullable=False)
    assets = db.relationship('Asset', backref='portfolio', lazy=True)

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    valuation = db.Column(db.Float, nullable=False)
    annual_return = db.Column(db.Float, nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

# Routes
@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))

    portfolios = Portfolio.query.all()
    for portfolio in portfolios:
        assets = Asset.query.filter_by(portfolio_id=portfolio.id).all()
        portfolio.net_worth = sum(asset.valuation for asset in assets)  # Calculate net worth

    response = make_response(render_template('index.html', username=session['user'], portfolios=portfolios))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route('/add_portfolio', methods=['GET', 'POST'])
def add_portfolio():
    if request.method == 'POST':
        owner_name = request.form['owner_name']
        assets_json = request.form['assets_json']
        assets_data = json.loads(assets_json)

        # Create portfolio
        new_portfolio = Portfolio(owner_name=owner_name)
        db.session.add(new_portfolio)
        db.session.commit()

        # Add assets to portfolio
        for asset in assets_data:
            new_asset = Asset(
                name=asset['name'],
                valuation=asset['valuation'],
                annual_return=asset['annualReturn'],
                portfolio_id=new_portfolio.id
            )
            db.session.add(new_asset)

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_portfolio.html')

@app.route('/delete_portfolio/<int:portfolio_id>', methods=['POST', 'GET'])
def delete_portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)

    # Manually delete associated assets
    for asset in portfolio.assets:
        db.session.delete(asset)

    db.session.delete(portfolio)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_asset/<int:portfolio_id>', methods=['GET', 'POST'])
def add_asset(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    if request.method == 'POST':
        asset_type = request.form['asset_type']
        custom_asset = request.form.get('custom_asset', '').strip()
        
        try:
            valuation = float(request.form['valuation'])
            annual_return = float(request.form['annual_return'])
        except ValueError:
            flash("Invalid input for valuation or annual return.", "danger")
            return redirect(request.url)

        asset_name = custom_asset if asset_type == "Other" else asset_type

        # Ensure asset is unique (case-insensitive)
        existing_asset = Asset.query.filter(
            func.lower(Asset.name) == asset_name.lower(),
            Asset.portfolio_id == portfolio_id
        ).first()
        if existing_asset:
            flash("Asset already exists in the portfolio!", "danger")
            return redirect(request.url)

        new_asset = Asset(name=asset_name, valuation=valuation, annual_return=annual_return, portfolio_id=portfolio_id)
        db.session.add(new_asset)
        db.session.commit()
        return redirect(url_for('view_portfolio', portfolio_id=portfolio_id))

    return render_template('add_asset.html', portfolio=portfolio)

@app.route('/delete_asset/<int:asset_id>/<int:portfolio_id>')
def delete_asset(asset_id, portfolio_id):
    asset = Asset.query.get_or_404(asset_id)
    db.session.delete(asset)
    db.session.commit()
    return redirect(f'/view_portfolio/{portfolio_id}')

@app.route('/edit_asset/<int:asset_id>/<int:portfolio_id>', methods=['GET', 'POST'])
def edit_asset(asset_id, portfolio_id):
    asset = Asset.query.get_or_404(asset_id)
    if request.method == 'POST':
        asset.name = request.form['name'].strip().lower()
        asset.valuation = float(request.form['valuation'])
        asset.annual_return = float(request.form['annual_return'])
        db.session.commit()
        return redirect(f'/view_portfolio/{portfolio_id}')
    return render_template('edit_asset.html', asset=asset, portfolio_id=portfolio_id)


@app.route('/view_portfolio/<int:portfolio_id>')
def view_portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    assets = Asset.query.filter_by(portfolio_id=portfolio_id).all()
    networth = sum([asset.valuation for asset in assets])
    projections = {asset.name: asset.valuation for asset in assets}
    asset_projections = calculate_future_projections(assets)
    #return render_template('view_portfolio.html', portfolio=portfolio, assets=assets, networth=networth, projections=projections)
    return render_template('view_portfolio.html', portfolio=portfolio, networth=networth, assets=assets, projections=projections, asset_projections=asset_projections)

def calculate_future_projections(assets):
    future_projections = {}
    for asset in assets:
        values = []
        future_value = asset.valuation
        for _ in range(5):  # Next 5 years
            future_value += (future_value * (asset.annual_return / 100))
            values.append(round(future_value, 2))
        future_projections[asset.name] = values
    return future_projections

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True, use_reloader=True)

