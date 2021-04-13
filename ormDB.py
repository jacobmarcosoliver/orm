from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///orm.db', 
echo = True,
check_same_thread=False
) 



Session = sessionmaker(bind = engine)
session = Session()

 Base = declarative_base()

class Children(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   dad_id = Column(Integer, ForeignKey('dads.id'))
   name = Column(String(10))
   city = Column(String(10))
   dad = relationship('Dad', back_populates='child')

class Dad(Base):
    __tablename__ = 'dads'

    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    child = relationship('Children', back_populates='dad')


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
 

hamid = Dad(
    name='hamid',
    child = [
        Children(name='ali', city='ahvaz'),
        Children(name='abbas', city='ahvaz')
    ]
)

# session.add(hamid)
# session.commit()

dad = session.query(Dad).first()
# # dad.child.name = 'abbas'
# # session.commit()

for child in dad.child:
    print(child.name, child.city)
