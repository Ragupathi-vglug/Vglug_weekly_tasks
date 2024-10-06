# DATA ENCAPSULATION
try:
    class university:
        def __init__(self):
            self.university_name="Annamalai University"
            self.place="Sidhambaram"
            self.university_code="214 806"
            self.login_id="codecs183"
            self.login_pass=9013988709
   
    o1=university()
    print(o1.university_name)
    print(o1.place)
    print(o1.university_code)
    print(o1.__login_id)
    print(o1.__login_pass)
except Exception:
    print("the given data is restricted for you to access")
