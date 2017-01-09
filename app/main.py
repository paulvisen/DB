
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String,TEXT,VARCHAR,DATETIME
from sqlalchemy.ext.declarative import declarative_base

from model import Report
from modelV2 import  ReportV2
ORIGINAL_DB_CONNECT_STRING = 'mysql+mysqldb://yuan:zhang123@115.28.190.18/flasktestdb?charset=utf8'
New_DB_CONNECT_STRING ='mysql+mysqldb://root:qwer@localhost/weme?charset=utf8'


engine_original = create_engine(ORIGINAL_DB_CONNECT_STRING)
engine_now = create_engine(New_DB_CONNECT_STRING)
DBSession_original = sessionmaker(bind=engine_original)
DBSession_now = sessionmaker(bind=engine_now)
session1 = DBSession_original()
session2 = DBSession_now()

#因为主键关系的存在，按照如下的步骤导出对应的数据
# 1. avatar  头像
# 2. user  用户
# 3. activity 活动
# 4. activityimage 活动照片
# 5. android_version 安卓版本
# 6. checkmsg 短信验证
# 7. topic 话题
# 8. post 文章
# 9. comment 评论
# 10. comment_image 评论图片
# 11. follow_id 关注
# 12. foodcard 食物照片
# 13. like_user_id 喜欢关系
# 14. message消息
# 15. message_image 图片消息
# 16. post_image 文章图片
# 17. poseter_image 海报照片
# 18. Report 举报
# 19. topic_image 话题照片
# 20. user_attend_activity_realtion 用户参加活动关系
# 21. user_image 用户照片
# 22. user_activity_relation 用户活动关系
# 23. user_like_activity_relation 用户喜欢关系表
# 24. user_like_foodcard  用户食物卡片喜欢关系
# 25. user_like_post  用户文章喜欢关系
# 26. user_visit 用户访问关系
#
#

query =session1.query(Report)



# for report in query:
#     print report.id
#     print report.authorid
#     print report.body
#     print report.type
#     print report.typeid
#     print report.timestamp

for report in query:
    reportv2 =ReportV2(authorid=report.authorid,body=report.body,type=report.type,typeid=report.typeid,timestamp=report.timestamp)
    session2.add(reportv2)
session2.commit()