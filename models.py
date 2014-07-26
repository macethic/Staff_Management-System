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

    def __init__(self, UG_Ins_Name, UG_Ins_Special, UG_Ins_Year, UG_Attach, PG_Ins_Name, PG_Ins_Special, PG_Ins_Year,\
	    PG_Attach, PHD_Ins_Name, PHD_Ins_Special, PHD_Ins_Year, PHD_Attach):

	self.UG_Ins_Name = UG_Ins_Name
	self.UG_Ins_Special = UG_Ins_Special
	self.UG_Ins_Year = UG_Ins_Year
	self.UG_Attach = UG_Attach

	self.PG_Ins_Name = PG_Ins_Name
	self.PG_Ins_Special = PG_Ins_Special
	self.PG_Ins_Year = PG_Ins_Year
	self.PG_Attach = PG_Attach

	self.PHD_Ins_Name = PHD_Ins_Name
	self.PHD_Ins_Special = PHD_Ins_Special
	self.PHD_Ins_Year = PHD_Ins_Year
	self.PHD_Attach = PHD_Attach


class Activities(db.Model):
    __tablename__ = 'Activities'

    AID = db.Column(db.Integer, primary_key=True)
    SID_Act = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    Workshops = db.Column(db.Text)
    Seminars = db.Column(db.Text)
    EDP = db.Column(db.Text, nullable=True)

    def __init__(self, Workshops, Seminars, EDP):
        
        self.Workshops = Workshops
	self.Seminars = Seminars
	self.EDP = EDP


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

    def __init__(self, TeachingExp_Name, TeachingExp_Desig, TeachingExp_FYear, TeachingExp_TYear,\
		    TeachingExp_Name1, TeachingExp_Desig1, TeachingExp_FYear1, TeachingExp_TYear1,\
		    TeachingExp_Name2, TeachingExp_Desig2, TeachingExp_FYear2, TeachingExp_TYear2,\
		    TeachingExp_Name3, TeachingExp_Desig3, TeachingExp_FYear3, TeachingExp_TYear3,\
		    TeachingExp_Name4, TeachingExp_Desig4, TeachingExp_FYear4, TeachingExp_TYear4):
    
	self.TeachingExp_Name = TeachingExp_Name
	self.TeachingExp_Desig = TeachingExp_Desig
	self.TeachingExp_FYear = TeachingExp_FYear
	self.TeachingExp_TYear = TeachingExp_TYear

	self.TeachingExp_Name1 = TeachingExp_Name1
	self.TeachingExp_Desig1 = TeachingExp_Desig1
	self.TeachingExp_FYear1 = TeachingExp_FYear1
	self.TeachingExp_TYear1 = TeachingExp_TYear1

	self.TeachingExp_Name2 = TeachingExp_Name2
	self.TeachingExp_Desig2 = TeachingExp_Desig2
	self.TeachingExp_FYear2 = TeachingExp_FYear2
	self.TeachingExp_TYear2 = TeachingExp_TYear2

        self.TeachingExp_Name3 = TeachingExp_Name3
	self.TeachingExp_Desig3 = TeachingExp_Desig3
	self.TeachingExp_FYear3 = TeachingExp_FYear3
	self.TeachingExp_TYear3 = TeachingExp_TYear3

        self.TeachingExp_Name4 = TeachingExp_Name4
	self.TeachingExp_Desig4 = TeachingExp_Desig4
	self.TeachingExp_FYear4 = TeachingExp_FYear4
	self.TeachingExp_TYear4 = TeachingExp_TYear4



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

    def __init__(self, Pub_Title, Pub_Year, Pub_Attach,\
		    Pub_Title1, Pub_Year1, Pub_Attach1,\
		    Pub_Title2, Pub_Year2, Pub_Attach2, 
		    Pub_Title3, Pub_Year3, Pub_Attach3,\
		    Pub_Title4, Pub_Year4, Pub_Attach4):
        
	self.Pub_Title = Pub_Title
	self.Pub_Year = Pub_Year
	self.Pub_Attach = Pub_Attach

 	self.Pub_Title1 = Pub_Title1
	self.Pub_Year1 = Pub_Year1
	self.Pub_Attach1 = Pub_Attach1

	self.Pub_Title2 = Pub_Title2
	self.Pub_Year2 = Pub_Year2
	self.Pub_Attach2 = Pub_Attach2

	self.Pub_Title3 = Pub_Title3
	self.Pub_Year3 = Pub_Year3
	self.Pub_Attach3 = Pub_Attach3

	self.Pub_Title4 = Pub_Title4
	self.Pub_Year4 = Pub_Year4
	self.Pub_Attach4 = Pub_Attach4


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

    def __init__(self, GLec_Name, GLec_Topic, GLec_Year,\
		    GLec_Name1, GLec_Topic1, GLec_Year1,\
		    GLec_Name2, GLec_Topic2, GLec_Year2,\
		    GLec_Name3, GLec_Topic3, GLec_Year3,\
		    GLec_Name4, GLec_Topic4, GLec_Year4):
        
	self.GLec_Name = GLec_Name
	self.GLec_Topic = GLec_Topic
	self.GLec_Year = GLec_Year
	
	self.GLec_Name1 = GLec_Name1
	self.GLec_Topic1 = GLec_Topic1
	self.GLec_Year1 = GLec_Year1
      
        self.GLec_Name2 = GLec_Name2
	self.GLec_Topic2 = GLec_Topic2
	self.GLec_Year2 = GLec_Year2

	self.GLec_Name3 = GLec_Name3
	self.GLec_Topic3 = GLec_Topic3
	self.GLec_Year3 = GLec_Year3
	
	self.GLec_Name4 = GLec_Name4
	self.GLec_Topic4 = GLec_Topic4
	self.GLec_Year4 = GLec_Year4


class Re_bodies_awards(db.Model):
    __tablename__ = 'Re_bodies_awards'
    
    RID = db.Column(db.Integer, primary_key=True)
    SID_Res = db.Column(db.Integer, db.ForeignKey('Staff.SID'))
    
    Research = db.Column(db.Text)
    ProfBodies = db.Column(db.Text)
    Awards = db.Column(db.Text)
    
    def __init__(self, Research, ProfBodies, Awards):
        
	self.Research = Research
	self.ProfBodies = ProfBodies
	self.Awards = Awards

class BookPublications(db.Model):
    __tablename__ = 'BookPublications'
    
    BID = db.Column(db.Integer, primary_key=True)
    SID_Book = db.Column(db.Integer, db.ForeignKey('Staff.SID'))
    
    Book_Name = db.Column(db.String(500))
    Book_Pub = db.Column(db.String(500))
    Book_ISBN = db.Column(db.String(500))
    Book_Year = db.Column(db.Integer, index=True)

    def __init__(self, Book_Name, Book_Pub, Book_ISBN, Book_Year):
        
	self.Book_Name = Book_Name
	self.Book_Pub = Book_Pub
	self.Book_ISBN = Book_ISBN
	self.Book_Year = Book_Year

class Others(db.Model):
    __tablename__ = 'Others'
	
    OID = db.Column(db.Integer, primary_key=True)
    SID_Others = db.Column(db.Integer, db.ForeignKey('Staff.SID'))

    Others = db.Column(db.Text)

    def __init__(self,Others):
	
	self.Others = Others





















    

