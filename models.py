from app import db


class Staff(db.Model):
    __tablename__ = 'Staff'

    SID = db.Column(db.Integer, primary_key=True)

    Staff_Name = db.Column(db.String(500), index=True)
    Staff_ID = db.Column(db.String(500), index=True, unique=True)
    Staff_Email = db.Column(db.String(500))
    Staff_Phone = db.Column(db.Integer, unique=True)
    Staff_Address = db.Column(db.Text)
    Staff_Photo = db.Column(db.Text)
    
    def __init__(self, Staff_Name, Staff_ID, Staff_Email, Staff_Phone, Staff_Address, Staff_Photo):
	    self.Staff_Name = Staff_Name
	    self.Staff_ID = Staff_ID
	    self.Staff_Email = Staff_Email
	    self.Staff_Phone = Staff_Phone
	    self.Staff_Address = Staff_Address
	    self.Staff_Photo = Staff_Photo


class Education(db.Model):
    __tablename__ = 'Education'
    
    EID = db.Column(db.Integer, primary_key=True)
    SID_Edu = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    UG_Ins_Name = db.Column(db.String(500))
    UG_Ins_Special = db.Column(db.String(500))
    UG_Ins_Year = db.Column(db.Integer)
    UG_Attach = db.Column(db.Text)

    PG_Ins_Name = db.Column(db.String(500))
    PG_Ins_Special = db.Column(db.String(500))
    PG_Ins_Year = db.Column(db.Integer)
    PG_Attach = db.Column(db.Text)

    PHD_Ins_Name = db.Column(db.String(500), nullable=True)
    PHD_Ins_Special = db.Column(db.String(500), nullable=True)
    PHD_Ins_Year = db.Column(db.Integer, nullable=True)
    PHD_Attach = db.Column(db.Text, nullable=True)


class Activities(db.Model):
    __tablename__ = 'Activities'

    AID = db.Column(db.Integer, primary_key=True)
    SID_Act = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    Workshops = db.Column(db.Text)
    Seminars = db.Column(db.Text)
    EDP = db.Column(db.Text, nullable=True)


class Experience(db.Model):
    __tablename__ = 'Experience'

    ExID = db.Column(db.Integer, primary_key=True)
    SID_Exp = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    TeachingExp_Name = db.Column(db.String(500))
    TeachingExp_Desig = db.Column(db.String(500))
    TeachingExp_FYear = db.Column(db.Integer)
    TeachingExp_TYear = db.Column(db.Integer)

    TeachingExp_Name1 = db.Column(db.String(500), nullable=True)
    TeachingExp_Desig1 = db.Column(db.String(500), nullable=True)
    TeachingExp_FYear1 = db.Column(db.Integer, nullable=True)
    TeachingExp_TYear1 = db.Column(db.Integer, nullable=True)
	
    TeachingExp_Name2 = db.Column(db.String(500), nullable=True)
    TeachingExp_Desig2 = db.Column(db.String(500), nullable=True)
    TeachingExp_FYear2 = db.Column(db.Integer, nullable=True)
    TeachingExp_TYear2 = db.Column(db.Integer, nullable=True)

    TeachingExp_Name3 = db.Column(db.String(500), nullable=True)
    TeachingExp_Desig3 = db.Column(db.String(500), nullable=True)
    TeachingExp_FYear3 = db.Column(db.Integer, nullable=True)
    TeachingExp_TYear3 = db.Column(db.Integer, nullable=True)

    TeachingExp_Name4 = db.Column(db.String(500), nullable=True)
    TeachingExp_Desig4 = db.Column(db.String(500), nullable=True)
    TeachingExp_FYear4 = db.Column(db.Integer, nullable=True)
    TeachingExp_TYear4 = db.Column(db.Integer, nullable=True)


class Publications(db.Model):
    __tablename__ = 'Publications'

    PID = db.Column(db.Integer, primary_key=True)
    SID_Pub = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    Pub_Title = db.Column(db.String(500))
    Pub_Year = db.Column(db.Integer, index=True)
    Pub_Attach = db.Column(db.Text)

    Pub_Title1 = db.Column(db.String(500), nullable=True)
    Pub_Year1 = db.Column(db.Integer, index=True, nullable=True)
    Pub_Attach1 = db.Column(db.Text, nullable=True)

    Pub_Title2 = db.Column(db.String(500), nullable=True)
    Pub_Year2 = db.Column(db.Integer, index=True, nullable=True)
    Pub_Attach2 = db.Column(db.Text, nullable=True)

    Pub_Title3 = db.Column(db.String(500), nullable=True)
    Pub_Year3 = db.Column(db.Integer, index=True, nullable=True)
    Pub_Attach3 = db.Column(db.Text, nullable=True)

    Pub_Title4 = db.Column(db.String(500), nullable=True)
    Pub_Year4 = db.Column(db.Integer, index=True, nullable=True)
    Pub_Attach4 = db.Column(db.Text, nullable=True)


class GuestLecture(db.Model):
    __tablename__ = 'GuestLecture'

    PID = db.Column(db.Integer, primary_key=True)
    SID_Glec = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    GLec_Name = db.Column(db.String(500))
    GLec_Topic = db.Column(db.String(500))
    GLec_Year = db.Column(db.Integer, index=True)

    GLec_Name1 = db.Column(db.String(500), nullable=True)
    GLec_Topic1 = db.Column(db.String(500), nullable=True)
    GLec_Year1 = db.Column(db.Integer, index=True, nullable=True)

    GLec_Name2 = db.Column(db.String(500), nullable=True)
    GLec_Topic2 = db.Column(db.String(500), nullable=True)
    GLec_Year2 = db.Column(db.Integer, index=True, nullable=True)

    GLec_Name3 = db.Column(db.String(500), nullable=True)
    GLec_Topic3 = db.Column(db.String(500), nullable=True)
    GLec_Year3 = db.Column(db.Integer, index=True, nullable=True)

    GLec_Name4 = db.Column(db.String(500), nullable=True)
    GLec_Topic4 = db.Column(db.String(500), nullable=True)
    GLec_Year4 = db.Column(db.Integer, index=True, nullable=True)


class Re_bodies_awards(db.Model):
    __tablename__ = 'Re_bodies_awards'
    
    RID = db.Column(db.Integer, primary_key=True)
    SID_Res = db.Column(db.Integer, db.ForeignKey('Staff.SID'))
    
    Research = db.Column(db.Text)
    ProfBodies = db.Column(db.Text)
    Awards = db.Column(db.Text)
    

class BookPublications(db.Model):
    __tablename__ = 'BookPublications'
    
    BID = db.Column(db.Integer, primary_key=True)
    SID_Book = db.Column(db.Integer, db.ForeignKey('Staff.SID'))
    
    Book_Name = db.Column(db.String(500))
    Book_Pub = db.Column(db.String(500))
    Book_ISBN = db.Column(db.String(500))
    Book_Year = db.Column(db.Integer, index=True)


class Others(db.Model):
    __tablename__ = 'Others'
	
    OID = db.Column(db.Integer, primary_key=True)
    SID_Others = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    Others = db.Column(db.Text)























    

