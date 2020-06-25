import faker
import time
# Thu Jun 25 2020 11:02:42 GMT-0400 (Eastern Daylight Time)

randISODate = lambda : faker.Faker().date_time().isoformat()
randUNIXDate = lambda : time.mktime(faker.Faker().date_time().timetuple())