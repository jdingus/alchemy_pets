from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, Text, Table
from sqlalchemy.orm import relationship, backref

from sqlalchemy.orm import sessionmaker
 

Base = declarative_base()
print "base class generated: {}".format(Base) 

##############  MODELS #######################

class Species(Base):
    """
    domain model class for a Species
    """
    __tablename__ = 'species'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breeds = relationship('Breed', backref="species", cascade="all, delete-orphan")

    # methods
    def __repr__(self):
        return self.name                   

class Breed(Base):
    """
    domain model class for a Breed
    has a with many-to-one relationship Species
    """
    __tablename__ = 'breed'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False) 
    pets = relationship('Pet', backref='breed')

    # there's a back ref on species that let's you get from breed to species

    def __repr__(self):
        return "{}: {}".format(self.name, self.species) 


class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    website = Column(Text, nullable=False)
    pets = relationship('Pet', backref="shelter")

    def __repr__(self):
            return self.name

# our many-to-many association table, in our model *before* Pet class 
pet_person_table = Table('pet_person', Base.metadata,
    Column('pet_id', Integer, ForeignKey('pet.id'), nullable=False),
    Column('person_id', Integer, ForeignKey('person.id'), nullable=False)
)


class Pet(Base):
    __tablename__ = 'pet'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    breed_id = Column(Integer, ForeignKey('breed.id')) 
    shelter_id = Column(Integer, ForeignKey('shelter.id')) 

    # must be nullable, as some pets will be the roots of our trees!
    parent_id = Column(Integer, ForeignKey(id), nullable=True ) 
    children = relationship('Pet', backref=backref('parent', remote_side=id) )

    # mapped "owners" relationship on backref in Person
    
    def __repr__(self):
        return self.name       


class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    city = Column(String)
    email = Column(String)
    
    # mapped relationship, pet_person table must already be in scope!
    pets = relationship('Pet', secondary=pet_person_table, backref='owners')
    
    def __repr__(self):
        return self.name

########### GET YOU UP AND RUNNING WITH A SESSION ##################

def setup_session():

    engine = create_engine('sqlite:///test.db')
    "created engine: {}".format(engine) 
    Session = sessionmaker(bind=engine)
    db_session = Session()
    return db_session

