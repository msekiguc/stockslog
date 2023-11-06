from flask import Blueprint, render_template, request
import sqlalchemy
import mysql.connector
from pw import password
from sqlalchemy.ext.declarative import declarative_base


def insertStock(stockInfo):
    engine = sqlalchemy.create_engine(
        #TODO secure password
        'mysql+mysqlconnector://root:' + password + '@localhost:3306/stocks_log', echo=True)
    Base = declarative_base()
    class Stocks(Base):
        __tablename__ = 'stocks'
 
        stock_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
        company_id = sqlalchemy.Column(sqlalchemy.Integer)
        sector_id = sqlalchemy.Column(sqlalchemy.Integer)
        ticker = sqlalchemy.Column(sqlalchemy.String(length=5))
        price = sqlalchemy.Column(sqlalchemy.DECIMAL(10,2))
        datePurchased = sqlalchemy.Column(sqlalchemy.DATE)
 
        def __repr__(self):
            return "<stocks(stock_id='{0}', company_id='{1}', sector_id='{2}', ticker='{3}', price='{4}', datePurchased='{5}')>".format(
                                self.stock_id, self.company_id, self.sector_id, self.ticker, self.price, self.datePurchased, )
 
    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    newStock = Stocks(stock_id=0, company_id=0, sector_id=0, ticker=stockInfo.get("ticker"), price=stockInfo.get("price"), datePurchased=stockInfo.get("datePurchased"))
    session.add(newStock)

    session.commit()
    



views = Blueprint(__name__, "views")

@views.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        insertStock(request.form)

    return render_template("home.html")

@views.route("/stocks")
def stocks():
    return "stocks"

@views.route("/companies")
def companies():
    return "companies"

@views.route("/sector")
def sector():
    return "sector"