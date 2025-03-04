import pytest
from tests import NoneType
from api.database import return_driver_result_query


@pytest.fixture(scope="module")
def dr_feature(test_db):
    return "Mast_cells_resting"


@pytest.fixture(scope="module")
def dr_feature_id(test_db, dr_feature):
    from api.db_models import Feature

    (id,) = test_db.session.query(Feature.id).filter_by(name=dr_feature).one_or_none()
    return id


@pytest.fixture(scope="module")
def dr_mutation():
    return "ABL1:(NS)"


@pytest.fixture(scope="module")
def dr_mutation_id(test_db, dr_mutation):
    from api.db_models import Mutation

    (id,) = test_db.session.query(Mutation.id).filter_by(name=dr_mutation).one_or_none()
    return id


@pytest.fixture(scope="module")
def dr_code():
    return "(NS)"


@pytest.fixture(scope="module")
def dr_tag():
    return "BLCA"


@pytest.fixture(scope="module")
def dr_tag_id(test_db, dr_tag):
    from api.db_models import Tag

    (id,) = test_db.session.query(Tag.id).filter_by(name=dr_tag).one_or_none()
    return id


def test_DriverResult_with_relations(
    app,
    data_set,
    data_set_id,
    dr_feature,
    dr_feature_id,
    dr_mutation,
    dr_tag,
    dr_tag_id,
    dr_mutation_id,
):
    string_representation_list = []
    separator = ", "
    relationships_to_join = ["data_set", "feature", "mutation", "tag"]

    query = return_driver_result_query(*relationships_to_join)
    results = (
        query.filter_by(dataset_id=data_set_id)
        .filter_by(feature_id=dr_feature_id)
        .filter_by(mutation_id=dr_mutation_id)
        .filter_by(tag_id=dr_tag_id)
        .limit(3)
        .all()
    )

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        driver_result_id = result.id
        string_representation = "<DriverResult %r>" % driver_result_id
        string_representation_list.append(string_representation)
        assert result.data_set.id == data_set_id
        assert result.data_set.name == data_set
        assert result.feature.id == dr_feature_id
        assert result.feature.name == dr_feature
        assert result.mutation.id == dr_mutation_id
        assert result.mutation.name == dr_mutation
        assert result.tag.id == dr_tag_id
        assert result.tag.name == dr_tag
        assert type(result.p_value) is float or NoneType
        assert type(result.fold_change) is float or NoneType
        assert type(result.log10_p_value) is float or NoneType
        assert type(result.log10_fold_change) is float or NoneType
        assert type(result.n_mutants) is int or NoneType
        assert type(result.n_wildtype) is int or NoneType
        assert repr(result) == string_representation
    assert repr(results) == "[" + separator.join(string_representation_list) + "]"


def test_DriverResult_no_relations(
    app, data_set_id, dr_feature_id, dr_mutation_id, dr_tag_id
):
    query = return_driver_result_query()
    results = (
        query.filter_by(dataset_id=data_set_id)
        .filter_by(feature_id=dr_feature_id)
        .filter_by(mutation_id=dr_mutation_id)
        .filter_by(tag_id=dr_tag_id)
        .limit(3)
        .all()
    )

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results:
        assert type(result.data_set) is NoneType
        assert type(result.feature) is NoneType
        assert type(result.mutation) is NoneType
        assert type(result.tag) is NoneType
        assert result.dataset_id == data_set_id
        assert result.feature_id == dr_feature_id
        assert result.tag_id == dr_tag_id
        assert type(result.p_value) is float or NoneType
        assert type(result.fold_change) is float or NoneType
        assert type(result.log10_p_value) is float or NoneType
        assert type(result.log10_fold_change) is float or NoneType
        assert type(result.n_mutants) is int or NoneType
        assert type(result.n_wildtype) is int or NoneType
