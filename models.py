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


class Education(db.Model):
    __tablename__ = 'Education'
    
    UG_Ins_Name = db.Column(db.String(500))
    UG_Ins_Special = db.Column(db.String(500))
    UG_Ins_Year = db.Column(db.Integer)
    UG_Attach = db.Column(db.Text)

    PG_Ins_Name = db.Column(db.String(500))
    PG_Ins_Special = db.Column(db.String(500))
    PG_Ins_Year = db.Column(db.Integer)
    PG_Attach = db.Column(db.Text)

    PHD_Ins_Name = db.Column(db.String(500))
    PHD_Ins_Special = db.Column(db.String(500))
    PHD_Ins_Year = db.Column(db.Integer)
    PHD_Attach = db.Column(db.Text)


class Activities(db.Model):
    __tablename__ = 'Activities'

    Workshops = db.Column(db.Text)
    Seminars = db.Column(db.Text)
    EDP = db.Column(db.Text)


class Experience(db.Model):
    __tablename__ = 'Experience'

    TeachingExp_Name = db.Column(db.String(500))
    TeachingExp_Desig = db.Column(db.String(500))
    TeachingExp_FYear = db.Column(db.Integer)
    TeachingExp_TYear = db.Column(db.Integer)

    TeachingExp_Name1 = db.Column(db.String(500))
    TeachingExp_Desig1 = db.Column(db.String(500))
    TeachingExp_FYear1 = db.Column(db.Integer)
    TeachingExp_TYear1 = db.Column(db.Integer)
	
    TeachingExp_Name2 = db.Column(db.String(500))
    TeachingExp_Desig2 = db.Column(db.String(500))
    TeachingExp_FYear2 = db.Column(db.Integer)
    TeachingExp_TYear2 = db.Column(db.Integer)

    TeachingExp_Name3 = db.Column(db.String(500))
    TeachingExp_Desig3 = db.Column(db.String(500))
    TeachingExp_FYear3 = db.Column(db.Integer)
    TeachingExp_TYear3 = db.Column(db.Integer)

    TeachingExp_Name4 = db.Column(db.String(500))
    TeachingExp_Desig4 = db.Column(db.String(500))
    TeachingExp_FYear4 = db.Column(db.Integer)
    TeachingExp_TYear4 = db.Column(db.Integer)


class Publications(db.Model):
    __tablename__ = 'Publications'
	
    Pub_Title = db.Column(db.String(500))
    Pub_Year = db.Column(db.Integer, index=True)
    Pub_Attach = db.Column(db.Text)

    Pub_Title1 = db.Column(db.String(500))
    Pub_Year1 = db.Column(db.Integer, index=True)
    Pub_Attach1 = db.Column(db.Text)

    Pub_Title2 = db.Column(db.String(500))
    Pub_Year2 = db.Column(db.Integer, index=True)
    Pub_Attach2 = db.Column(db.Text)

    Pub_Title3 = db.Column(db.String(500))
    Pub_Year3 = db.Column(db.Integer, index=True)
    Pub_Attach3 = db.Column(db.Text)

    Pub_Title4 = db.Column(db.String(500))
    Pub_Year4 = db.Column(db.Integer, index=True)
    Pub_Attach4 = db.Column(db.Text)


class GuestLecture(db.Model):
    __tablename__ = 'GuestLecture'

    GLec_Name = db.Column(db.String(500))
    GLec_Topic = db.Column(db.String(500))
    GLec_Year = db.Column(db.Integer, index=True)

    GLec_Name1 = db.Column(db.String(500))
    GLec_Topic1 = db.Column(db.String(500))
    GLec_Year1 = db.Column(db.Integer, index=True)

    GLec_Name2 = db.Column(db.String(500))
    GLec_Topic2 = db.Column(db.String(500))
    GLec_Year2 = db.Column(db.Integer, index=True)

    GLec_Name3 = db.Column(db.String(500))
    GLec_Topic3 = db.Column(db.String(500))
    GLec_Year3 = db.Column(db.Integer, index=True)

    GLec_Name4 = db.Column(db.String(500))
    GLec_Topic4 = db.Column(db.String(500))
    GLec_Year4 = db.Column(db.Integer, index=True)


class Re_bodies_awards(db.Model):
    __tablename__ = 'Re_bodies_awards'
    
    Research = db.Column(db.Text)
    ProfBodies = db.Column(db.Text)
    Awards = db.Column(db.Text)
    

class Publications(db.Model):
    __tablename__ = 'Publications'
    
    Book_Name = db.Column(db.String(500))
    Book_Pub = db.Column(db.String(500))
    Book_ISBN = db.Column(db.String(500))
    Book_Year = db.Column(db.Integer, index=True)


class Others(db.Model):
    __tablename__ = 'Others'
	
    Others = db.Column(db.Text)























    

