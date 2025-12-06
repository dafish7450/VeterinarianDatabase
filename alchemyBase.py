# alchemyBase.py
from sqlalchemy import (
    Column, Integer, String, Float, DateTime, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Company(Base):
    __tablename__ = 'Company'
    companyID   = Column(Integer, primary_key=True)
    companyName = Column(String,  nullable=False)

    clinics     = relationship('Clinic', back_populates='company')

class Clinic(Base):
    __tablename__ = 'Clinic'
    clinicID      = Column(Integer, primary_key=True)
    clinicAddress = Column(String,  nullable=False)
    companyID     = Column(Integer, ForeignKey('Company.companyID'), nullable=False)
    clinicName    = Column(String,  nullable=False)

    company       = relationship('Company', back_populates='clinics')
    vets          = relationship('Veterinarian', back_populates='clinic')

class Veterinarian(Base):
    __tablename__ = 'Veterinarian'
    vetID     = Column(Integer, primary_key=True)
    vetName   = Column(String,  nullable=False)
    clinicID  = Column(Integer, ForeignKey('Clinic.clinicID'), nullable=False)

    clinic    = relationship('Clinic', back_populates='vets')
    visit    = relationship('Visit', back_populates='veterinarian')

class PetOwner(Base):
    __tablename__ = 'PetOwner'
    ownerID    = Column(Integer, primary_key=True)
    ownerFirst = Column(String,  nullable=False)
    ownerLast  = Column(String,  nullable=False)
    ownerEmail = Column(String,  nullable=False, unique=True)

    pets       = relationship('Pet',     back_populates='owner')
    billings   = relationship('Billing', back_populates='owner')

class Pet(Base):
    __tablename__ = 'Pet'
    petID      = Column(Integer, primary_key=True)
    petName    = Column(String,  nullable=False)
    petWeight  = Column(Float)
    petDOB  = Column(String, nullable=False)
    ownerID    = Column(Integer, ForeignKey('PetOwner.ownerID'), nullable=False)

    owner      = relationship('PetOwner', back_populates='pets')
    visit     = relationship('Visit',    back_populates='pet')

class Visit(Base):
    __tablename__ = 'Visit'
    visitID    = Column(Integer, primary_key=True)
    petID      = Column(Integer, ForeignKey('Pet.petID'),           nullable=False)
    vetID      = Column(Integer, ForeignKey('Veterinarian.vetID'),  nullable=False)
    date       = Column(String, nullable=False)

    pet         = relationship('Pet',          back_populates='visit')
    veterinarian= relationship('Veterinarian', back_populates='visit')
    billings    = relationship('Billing',      back_populates='visit')

class Billing(Base):
    __tablename__ = 'Billing'
    receiptID     = Column(Integer, primary_key=True)
    ownerID       = Column(Integer, ForeignKey('PetOwner.ownerID'),  nullable=False)
    billAmount    = Column(Integer, nullable=False)
    billAddress   = Column(String,  nullable=False)
    billInsurance = Column(String)
    visitID       = Column(Integer, ForeignKey('Visit.visitID'),    nullable=False)

    owner         = relationship('PetOwner', back_populates='billings')
    visit         = relationship('Visit',   back_populates='billings')








