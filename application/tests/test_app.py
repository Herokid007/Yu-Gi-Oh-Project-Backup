from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import MonsterName, MonsterType

#Creating the tese base class
class TestBase(TestCase):
    def create_app(self):

        #Pass in the testing config for the database app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", SECRET_KEY='TEST_SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        #Creates a table
        db.create_all()
        #Creates a test for duel monster name
        name1 = MonsterName("Test-Duel-Monster-Name")
        #The information is stored in the database
        db.session.add(name1)
        db.session.commit()
        #Creates test for duel monster type
        type1 = MonsterType(mtype = 'Test-Spellcaster-Type', fk_typeid = name1.id)
        db.session.add(type1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

#Inspects a test class for adding & updating Duel Monster name & type
#User will not be able run a GET request for delete & update

#Test sending a GET request for the index.html page
class TestIndexPage(TestBase):
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test-007', response.data)

#Test sending a GET request to add Duel Monster name
class TestAddName1(TestBase):
    def test_add_name1(self):
        response = self.client.get(url_for('addname'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Adding test: Duel-Monster name1', response.data)
        
#Test adding Duel Monster name
class TestAddName2(TestBase):
    def test_add_name2(self):
        response = self.client.post(url_for('addname', id=1),data = dict(q_name='Elemental-Hero-Flame-Wingman-Test'), follow_redirects=True)
        self.assertIn(b'Adding test: Duel-Monster name2 ',response.data)

#Test sending a GET request to add Duel Monster type
class TestAddType1(TestBase):
    def test_add_type1(self):
        response = self.client.get(url_for('addtype'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Adding test: Duel-Monster type1', response.data)

#Test adding a Duel Monster type
class TestAddType2(TestBase):
    def test_add_type2(self):
        response = self.client.post(url_for('addtype'), data = dict(q_type="Warrior-Test"), follow_redirects=True)
        self.assertIn(b'Adding test: Duel-Monster type2',response.data)

#Test sending a GET request to update Duel Monster name
class TestUpdateName1(TestBase):
    def test_update_name1(self):
        response = self.client.get(url_for('updatename', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updating test: Duel-Monster name1', response.data)
        
# Test updating te Duel M
class TestUpdateName2(TestBase):
    def test_update_name2(self):
        response = self.client.post(url_for('updatename'), data = dict(q_type="Dark-Magician-Test"), follow_redirects=True)
        self.assertIn(b'Adding test: Duel-Monster type2',response.data)

# Test sending a GET request to the add options page
class TestUpdateType1(TestBase):
    def test_update_type1(self):
        response = self.client.get(url_for('updatetype', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updating test: Duel-Monster type1', response.data)

# Test adding a question
class TestUpdateType2(TestBase):
    def test_update_type2(self):
        response = self.client.post(url_for('updatetype'), data = dict(q_type="Spellcaster-Test"), follow_redirects=True)
        self.assertIn(b'Updating test: Duel-Monster type2',response.data)







# Test Deleting an option
class TestDelo(TestBase):
    def test_del_o(self):
        response = self.client.get(url_for('delete_o', oid = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Testq', response.data)
        self.assertNotIn(b'This is a test option', response.data)

# Test Deleting a question
class TestDelq(TestBase):
    def test_del_q(self):
        response = self.client.get(url_for('delete_q', qid = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Testq', response.data)
