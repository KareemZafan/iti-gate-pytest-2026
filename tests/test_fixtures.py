import pytest

# @pytest.fixture(scope="module",autouse=True)
# def test_connectToDB():
#     ## code to set up the database connection
#     print("\nOpening DB connection ....")

# @pytest.fixture(scope="module",autouse=True)
# def test_closeDBConnection():
#     yield
#     ## Close the database connection
#     print("\nClosing DB connection ....")

@pytest.fixture(scope="module",autouse=True)
def setup_DB_connection():
    ## code to set up the database connection
    print("\nOpening DB connection ....")
    yield
    ## Close the database connection
    print("\nClosing DB connection ....")

def test_insertInotDB(): 
    print("\nInserting ....")
    assert True

def test_updadteRowInDB(): 
    print("\nUpdating ....")
    assert True

def test_deletingFromDB(): 
    print("\nDeleting ....")
    assert True
