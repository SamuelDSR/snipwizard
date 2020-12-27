from snipwizard.option import Option, Nothing


class TestOptionClass:
    def __init__(self, v):
        self.v = v

    def add(self, v):
        print(f"inside add:{v}")
        return v + self.v
    
    @property
    def val_add_10(self):
        return self.v + 10


def test_some():
    s = Option(TestOptionClass(10))
    assert s.foo() == Nothing()
    assert s.foobar(100) == Nothing()
    assert s.add(10) == Option(20)
    assert s.val_add_10 == Option(20)
    assert s.val_add_10.some_props == Nothing()
    assert s.getOrElse(TestOptionClass(20)).v == 10
    assert s["age"] == Nothing()

    d = {
        "person": {
            "name": "sam",
            "age": 20,
        },
        "company": {
            "name": "veepee",
        }
    }
    d = Option(d)
    assert d["address"] == Nothing()
    assert d["person"]["name"] == Option("sam")
    assert d["person"]["role"] == Nothing()
    assert d["person"]["age"].getOrElse(0) == 20
    assert d["company"]["name"].getOrElse("adomik") == "veepee"
