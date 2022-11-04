from bunnet.odm.operators.update.general import Max
from bunnet.odm.queries.update import UpdateQuery, UpdateMany
from tests.models import Sample


def test_set(session):
    q = Sample.find_many(Sample.integer == 1).set(
        {Sample.integer: 100}, session=session
    )

    assert isinstance(q, UpdateQuery)
    assert isinstance(q, UpdateMany)
    assert q.session == session

    assert q.update_query == {"$set": {"integer": 100}}

    q = (
        Sample.find_many(Sample.integer == 1)
        .update(Max({Sample.integer: 10}))
        .set({Sample.integer: 100})
    )

    assert isinstance(q, UpdateQuery)
    assert isinstance(q, UpdateMany)

    assert q.update_query == {
        "$max": {"integer": 10},
        "$set": {"integer": 100},
    }


def test_current_date(session):
    q = Sample.find_many(Sample.integer == 1).current_date(
        {Sample.timestamp: "timestamp"}, session=session
    )

    assert isinstance(q, UpdateQuery)
    assert isinstance(q, UpdateMany)
    assert q.session == session

    assert q.update_query == {"$currentDate": {"timestamp": "timestamp"}}

    q = (
        Sample.find_many(Sample.integer == 1)
        .update(Max({Sample.integer: 10}))
        .current_date({Sample.timestamp: "timestamp"})
    )

    assert isinstance(q, UpdateQuery)
    assert isinstance(q, UpdateMany)

    assert q.update_query == {
        "$max": {"integer": 10},
        "$currentDate": {"timestamp": "timestamp"},
    }


def test_inc(session):
    q = Sample.find_many(Sample.integer == 1).inc(
        {Sample.integer: 100}, session=session
    )

    assert isinstance(q, UpdateQuery)
    assert isinstance(q, UpdateMany)
    assert q.session == session

    assert q.update_query == {"$inc": {"integer": 100}}

    q = (
        Sample.find_many(Sample.integer == 1)
        .update(Max({Sample.integer: 10}))
        .inc({Sample.integer: 100})
    )

    assert isinstance(q, UpdateQuery)
    assert isinstance(q, UpdateMany)

    assert q.update_query == {
        "$max": {"integer": 10},
        "$inc": {"integer": 100},
    }
