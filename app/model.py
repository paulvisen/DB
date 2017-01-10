# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String,TEXT,VARCHAR,DATETIME,BOOLEAN,DateTime,UnicodeText,Text
from sqlalchemy.ext.declarative import declarative_base

from modelV2 import *


BaseModel = declarative_base()


class AvatarVoice(BaseModel):
    __tablename__='avatarvoices'

    id = Column(Integer,primary_key=True)
    userid = Column(Integer)
    avatarurl = Column(VARCHAR)
    voiceurl = Column(VARCHAR)
    avatar_number = Column(Integer)
    voice_number = Column(Integer)
    cardflag = Column(BOOLEAN)
    disable = Column(BOOLEAN)
    gender = Column(VARCHAR)
    name = Column(VARCHAR)


def findAvatarVoiceById(self, userv2):
    try:
        temp = AvatarVoice.query.filter_by(userid=userv2.id).first()
        if temp is None:
            return None
        else:
            return temp
    except Exception, e:
        return None


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR )
    password = Column(VARCHAR)
    token = Column(VARCHAR)
    school = Column(VARCHAR)
    degree = Column(VARCHAR)
    department = Column(VARCHAR)
    enrollment = Column(VARCHAR)
    name = Column(VARCHAR)
    gender = Column(VARCHAR)
    phone = Column(VARCHAR)
    birthday = Column(VARCHAR)
    wechat = Column(VARCHAR)
    qq = Column(VARCHAR)
    hometown = Column(VARCHAR)
    hobby = Column(VARCHAR)
    preference = Column(VARCHAR)
    lookcount = Column(Integer, default=0)
    cardflag = Column(BOOLEAN, default=False)
    weme = Column(Integer, default=100)
    certification = Column(BOOLEAN, default = False)
    tags = Column(UnicodeText)


class Activity(BaseModel):
    __tablename__='activitys'
    id = Column(Integer, primary_key=True)
    top = Column(VARCHAR, default='0')
    title = Column(VARCHAR, primary_key=True)
    time = Column(VARCHAR)
    location = Column(VARCHAR)
    number = Column(VARCHAR)
    signnumber = Column(Integer)
    state = Column(VARCHAR)
    sponsor = Column(VARCHAR)
    disable = Column(BOOLEAN, default=False)
    remark = Column(String(32))
    authorid = Column(Integer)
    whetherimage = Column(BOOLEAN, default=False)
    advertise = Column(String(32))
    detail = Column(Text)
    label = Column(String(32))
    passflag = Column(String(8), default='0')
    likenumber = Column(Integer, default=0)
    timestamp =Column(DateTime)

class ActivityImage(BaseModel):
    __tablename__='activityimageattachs'
    id =Column(Integer,primary_key=True)
    activityid = Column(Integer,primary_key=True)
    imageid = Column(Integer,primary_key=True)
    timestamp = Column(DATETIME)


class AndroidVersions(BaseModel):
    __tablename__='androidversions'
    id = Column(Integer,primary_key=True)
    v1 = Column(Integer)
    v2 = Column(Integer)
    v3 = Column(Integer)
    disable = Column(BOOLEAN)
    wemeurl = Column(VARCHAR)
    timestamp = Column(DATETIME)


class CheckMsgs(BaseModel):
    __tablename__='checkMsgs'
    id = Column(Integer,primary_key=True)
    phone = Column(VARCHAR)
    code = Column(VARCHAR)
    timestamp = Column(DATETIME)

class Topic(BaseModel):
    __tablename__='topics'
    id = Column(Integer,primary_key=True)
    theme = Column(VARCHAR)
    imageurl = Column(VARCHAR)
    note = Column(VARCHAR)
    number = Column(Integer)
    postnumber = Column(Integer)
    rank = Column(Integer)
    slogan = Column(VARCHAR)



class Post(BaseModel):
    __tablename__='posts'
    id = Column(Integer,primary_key=True)
    title = Column(VARCHAR)
    body = Column(Text)
    timestamp = Column(DATETIME)
    authorid = Column(Integer)
    topicid = Column(Integer)
    likenumber =Column(Integer)
    commentnumber = Column(Integer)
    top = Column(Integer)
    disable = Column(BOOLEAN)


class LikeUser(BaseModel):
    __tablename__='likeusercards'
    id = Column(Integer,primary_key=True)
    likeid = Column(Integer)
    likedid = Column(Integer)
    timestamp = Column(DATETIME)


class FoodCard(BaseModel):
    __tablename__='foodcards'
    id = Column(Integer,primary_key=True)
    title  =Column(VARCHAR)
    authorid = Column(Integer)
    imageurl = Column(VARCHAR)
    location = Column(VARCHAR)
    longitude = Column(VARCHAR)
    latitude = Column(VARCHAR)
    price = Column(VARCHAR)
    comment = Column(VARCHAR)
    passflag = Column(VARCHAR)
    disable = Column(VARCHAR)
    timestamp = Column(DATETIME)
    likenumber = Column(Integer)

class Follow(BaseModel):
    __tablename__='follows'
    follower_id = Column(Integer,primary_key=True)
    followed_id = Column(Integer,primary_key=True)
    timestamp = Column(DATETIME)





# class Report(BaseModel):
#     __tablename__ = 'reports'
#
#     id = Column(Integer, primary_key=True)
#     authorid = Column(Integer)
#     body = Column(TEXT)
#     type = Column(VARCHAR)
#     typeid = Column(Integer)
#     timestamp = Column(DATETIME)