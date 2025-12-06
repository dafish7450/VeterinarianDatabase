
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemyBase import Base, Pet, PetOwner, Clinic, Company, Veterinarian, Visit, Billing

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')

engine = create_engine('sqlite:///DBproj.db')
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def home():
    return render_template('home.html')


## VIEW DATA

## Owner
@app.route("/ownerView")
def show_owner():
    owners = session.query(PetOwner).all()
    columns = PetOwner.__table__.columns.keys()
    return render_template("ownerView.html", owners=owners, columns=columns, getattr=getattr)

## Pets
@app.route("/petsView")
def show_pets():
    pets = session.query(Pet).all()
    columns = Pet.__table__.columns.keys()
    return render_template("petsView.html", pets=pets, columns=columns, getattr=getattr)

## Vet
@app.route("/vetView")
def show_vets():
    vets = session.query(Veterinarian).all()
    columns = Veterinarian.__table__.columns.keys()
    return render_template("vetView.html", vets=vets, columns=columns, getattr=getattr)

## Visit
@app.route("/visitView")
def show_visits():
    visits = session.query(Visit).all()
    columns = Visit.__table__.columns.keys()
    return render_template("visitView.html", visits=visits, columns=columns, getattr=getattr)

## Billing
@app.route("/billingView")
def show_billing():
    billing = session.query(Billing).all()
    columns = Billing.__table__.columns.keys()
    return render_template("billingView.html", billing=billing, columns=columns, getattr=getattr)

## Clinic
@app.route("/clinicView")
def show_clinics():
    clinics = session.query(Clinic).all()
    columns = Clinic.__table__.columns.keys()
    return render_template("clinicView.html", clinics=clinics, columns=columns, getattr=getattr)

## Company
@app.route("/companyView")
def show_companies():
    companies = session.query(Company).all()
    columns = Company.__table__.columns.keys()
    return render_template("companyView.html", companies=companies, columns=columns, getattr=getattr)

# ADD NEW DATA

## BILLING
@app.route("/billing/new", methods=["GET", "POST"])
def new_billing():
    owners = session.query(PetOwner).all()
    visits = session.query(Visit).all()

    if request.method == "POST":
        new_bill = Billing(
            ownerID=request.form["ownerID"],
            billAmount=request.form["billAmount"],
            billAddress=request.form["billAddress"],
            billInsurance=request.form["billInsurance"],
            visitID=request.form["visitID"]
        )
        session.add(new_bill)
        session.commit()
        return redirect(url_for('show_billing'))

    return render_template("new_billing.html", owners=owners, visits=visits)

## COMPANY
@app.route("/company/new", methods=["GET", "POST"])
def new_company():

    if request.method == "POST":
        new_company = Company(
            companyName=request.form["companyName"]
        )
        session.add(new_company)
        session.commit()
        return redirect(url_for('show_companies'))

    return render_template("new_company.html")

## CLINIC
@app.route("/clinic/new", methods=["GET", "POST"])
def new_clinic():

    companies = session.query(Company).all()

    if request.method == "POST":
        new_clinic = Clinic(
            clinicName=request.form["clinicName"],
            clinicAddress=request.form["clinicAddress"],
            companyID=request.form["companyID"]
        )
        session.add(new_clinic)
        session.commit()
        return redirect(url_for('show_clinics'))

    return render_template("new_clinic.html", companies=companies)

## VET
@app.route("/vet/new", methods=["GET", "POST"])
def new_vet():

    clinics = session.query(Clinic).all()

    if request.method == "POST":
        new_vet = Veterinarian(
            vetName=request.form["vetName"],
            clinicID=request.form["clinicID"]
        )
        session.add(new_vet)
        session.commit()
        return redirect(url_for('show_vets'))

    return render_template("new_vet.html", clinics=clinics)

## PET
@app.route("/pet/new", methods=["GET", "POST"])
def new_pet():

    owners = session.query(PetOwner).all()

    if request.method == "POST":
        new_pet = Pet(
            petName=request.form["petName"],
            petWeight=request.form["petWeight"],
            petDOB=request.form["petDOB"],
            ownerID=request.form["ownerID"]
        )
        session.add(new_pet)
        session.commit()
        return redirect(url_for('show_pets'))

    return render_template("new_pet.html", owners=owners)

## COMPANY
@app.route("/owner/new", methods=["GET", "POST"])
def new_owner():

    if request.method == "POST":
        new_owner = PetOwner(
            ownerFirst=request.form["ownerFirst"],
            ownerLast=request.form["ownerLast"],
            ownerEmail=request.form["ownerEmail"]
        )
        session.add(new_owner)
        session.commit()
        return redirect(url_for('show_owner'))

    return render_template("new_owner.html")

## VISIT
@app.route("/visit/new", methods=["GET", "POST"])
def new_visit():

    pets = session.query(Pet).all()
    vets = session.query(Veterinarian).all()

    if request.method == "POST":
        new_visit = Visit(
            petID=request.form["petID"],
            vetID=request.form["vetID"],
            date=request.form["date"],
        )
        
        session.add(new_visit)
        session.commit()
        return redirect(url_for('show_visits'))

    return render_template("new_visit.html", pets=pets, vets=vets)

## Related Info
@app.route("/view/<id_type>/<int:id_value>")
def view_details(id_type, id_value):
    owners = session.query(PetOwner).all()
    pets = session.query(Pet).all()
    visits = session.query(Visit).all()
    billings = session.query(Billing).all()
    veterinarians = session.query(Veterinarian).all()
    clinics = session.query(Clinic).all()
    companies = session.query(Company).all()

    return render_template(
        "details_view.html",
        id_type=id_type,
        id_value=id_value,
        owners=owners,
        pets=pets,
        visits=visits,
        billings=billings,
        veterinarians=veterinarians,
        clinics=clinics,
        companies=companies
    )

if __name__ == '__main__':
    app.run(debug=True)
