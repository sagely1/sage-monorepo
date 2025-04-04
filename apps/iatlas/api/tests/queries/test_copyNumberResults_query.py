import json
import pytest
from tests import NoneType
from api.enums import direction_enum
from api.resolvers.resolver_helpers.paging_utils import (
    from_cursor_hash,
    to_cursor_hash,
    Paging,
)

"""
query CopyNumberResults(
  $paging: PagingInput
  $distinct:Boolean
  $dataSet: [String!]
  $related: [String!]
  $feature: [String!]
  $entrez: [Int!]
  $tag: [String!]
  $direction: DirectionEnum
  $minPValue: Float
  $maxPValue: Float
  $minLog10PValue: Float
  $maxLog10PValue: Float
  $minMeanNormal: Float
  $minMeanCnv: Float
  $minTStat: Float
) {
  copyNumberResults(
    paging: $paging
    distinct: $distinct
    dataSet: $dataSet
    related: $related
    feature: $feature
    entrez: $entrez
    tag: $tag
    direction: $direction
    minPValue: $minPValue
    maxPValue: $maxPValue
    minLog10PValue: $minLog10PValue
    maxLog10PValue: $maxLog10PValue
    minMeanNormal: $minMeanNormal
    minMeanCnv: $minMeanCnv
    minTStat: $minTStat
  ) {
    paging {
      type
      pages
      total
      startCursor
      endCursor
      hasPreviousPage
      hasNextPage
      page
      limit
    }
    error
    items {
      id
      direction
      meanNormal
      meanCnv
      pValue
      log10PValue
      tStat
      dataSet {
        name
      }
      tag {
        name
      }
      gene {
        entrez
        hgnc
      }
      feature {
        name
      }
    }
  }
}
"""


@pytest.fixture(scope="module")
def test_cnr():
    return {
        "dataset": "TCGA",
        "tag": "C1",
        "entrez_id": 55303,
        "feature": "Subclonal_genome_fraction",
        "direction": "Amp",
    }


@pytest.fixture(scope="module")
def min_p_value():
    return 0.0000028


@pytest.fixture(scope="module")
def max_p_value():
    return 0.000021


@pytest.fixture(scope="module")
def min_log10_p_value():
    return 0.000037


@pytest.fixture(scope="module")
def max_log10_p_value():
    return 13.162428


@pytest.fixture(scope="module")
def min_mean_normal():
    return 9.313083


@pytest.fixture(scope="module")
def min_mean_cnv():
    return 14.833332


@pytest.fixture(scope="module")
def min_t_stat():
    return -5.118745


@pytest.fixture(scope="module")
def common_query_builder():
    def f(query_fields):
        return (
            """query CopyNumberResults(
            $paging: PagingInput
            $distinct:Boolean
            $dataSet: [String!]
            $related: [String!]
            $feature: [String!]
            $entrez: [Int!]
            $tag: [String!]
            $direction: DirectionEnum
            $minPValue: Float
            $maxPValue: Float
            $minLog10PValue: Float
            $maxLog10PValue: Float
            $minMeanNormal: Float
            $minMeanCnv: Float
            $minTStat: Float
        ) {
        copyNumberResults(
            paging: $paging
            distinct: $distinct
            dataSet: $dataSet
            related: $related
            feature: $feature
            entrez: $entrez
            tag: $tag
            direction: $direction
            minPValue: $minPValue
            maxPValue: $maxPValue
            minLog10PValue: $minLog10PValue
            maxLog10PValue: $maxLog10PValue
            minMeanNormal: $minMeanNormal
            minMeanCnv: $minMeanCnv
            minTStat: $minTStat
        )"""
            + query_fields
            + "}"
        )

    return f


# Test that forward cursor pagination gives us the expected pagingInfo


def test_copyNumberResults_cursor_pagination_first(client, common_query_builder):
    query = common_query_builder(
        """{
            paging {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
            }
            items { id }
        }"""
    )
    num = 10
    response = client.post(
        "/api", json={"query": query, "variables": {"paging": {"first": num}}}
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    items = page["items"]
    paging = page["paging"]
    start = from_cursor_hash(paging["startCursor"])
    end = from_cursor_hash(paging["endCursor"])

    assert len(items) == num
    assert paging["hasNextPage"] == True
    assert paging["hasPreviousPage"] == False
    assert start == items[0]["id"]
    assert end == items[num - 1]["id"]


def test_copyNumberResults_cursor_pagination_last(client, common_query_builder):
    query = common_query_builder(
        """{
            paging {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
            }
            items { id }
        }"""
    )
    num = 10
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {"paging": {"last": num, "before": to_cursor_hash(100)}},
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    items = page["items"]
    paging = page["paging"]
    start = from_cursor_hash(paging["startCursor"])
    end = from_cursor_hash(paging["endCursor"])

    assert len(items) == num
    assert paging["hasNextPage"] == False
    assert paging["hasPreviousPage"] == True
    assert start == items[0]["id"]
    assert end == items[num - 1]["id"]


def test_copyNumberResults_cursor_distinct_pagination(client, common_query_builder):
    query = common_query_builder(
        """{
            paging { page }
            items { pValue }
        }"""
    )
    page_num = 2
    num = 10
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "paging": {
                    "page": page_num,
                    "first": num,
                },
                "distinct": True,
                "dataSet": ["TCGA"],
                "tag": ["C1"],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    items = page["items"]

    assert len(items) == num
    assert page_num == page["paging"]["page"]


def test_copyNumberResults_missing_pagination(client, common_query_builder):
    """Verify that query does not error when paging is not sent by the client

    The purpose of this test is the ensure that valid and sensible default values
    are used and the query does not error, when no paging arguments are sent.
    Cursor pagination and a limit of 100,000 will be used by default.
    """
    query = common_query_builder("""{ items { pValue } }""")
    response = client.post(
        "/api", json={"query": query, "variables": {"dataSet": ["TCGA"]}}
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    items = page["items"]

    assert len(items) == 10000


def test_copyNumberResults_query_with_passed_data_set(
    client, common_query_builder, test_cnr
):
    query = common_query_builder(
        """{
            paging {
                total
                startCursor
                endCursor
                hasPreviousPage
                hasNextPage
            }
            items {
                dataSet { name }
            }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "paging": {"first": 10},
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "cnr_feature": [test_cnr["feature"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    paging = page["paging"]
    items = page["items"]

    assert type(paging["total"]) is int
    assert paging["hasNextPage"] == True
    assert paging["hasPreviousPage"] == False
    assert type(paging["startCursor"]) is str
    assert type(paging["endCursor"]) is str

    assert isinstance(items, list)
    assert len(items) > 0
    for item in items[0:2]:
        current_data_set = item["dataSet"]
        assert current_data_set["name"] == test_cnr["dataset"]


def test_copyNumberResults_query_with_passed_related(
    client, common_query_builder, test_cnr, min_t_stat, related
):
    query = common_query_builder(
        """{
            items { tStat }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minTStat": min_t_stat,
                "related": ["does_not_exist"],
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) == 0

    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minTStat": min_t_stat,
                "related": [related],
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["tStat"] >= min_t_stat


def test_copyNumberResults_query_with_passed_entrez(
    client, common_query_builder, test_cnr
):
    query = common_query_builder(
        """{
            items {
                gene { entrez }
            }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "feature": [test_cnr["feature"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        gene = result["gene"]
        assert gene["entrez"] == test_cnr["entrez_id"]


def test_copyNumberResults_query_with_passed_features(
    client, common_query_builder, test_cnr
):
    query = common_query_builder(
        """{
            items {
                feature { name }
            }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "feature": [test_cnr["feature"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        feature = result["feature"]
        assert feature["name"] == test_cnr["feature"]


def test_copyNumberResults_query_with_passed_tag(
    client, common_query_builder, test_cnr
):
    query = common_query_builder(
        """{
            items {
                tag { name }
            }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "feature": [test_cnr["feature"]],
                "tag": [test_cnr["tag"]],
                "paging": {"first": 100000},
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        tag = result["tag"]
        assert tag["name"] == test_cnr["tag"]


def test_copyNumberResults_query_with_passed_direction(
    client, common_query_builder, test_cnr
):
    query = common_query_builder(
        """{
            items { direction }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "direction": test_cnr["direction"],
                "entrez": [test_cnr["entrez_id"]],
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["direction"] == test_cnr["direction"]


def test_copyNumberResults_query_with_passed_min_p_value(
    client, common_query_builder, test_cnr, min_p_value
):
    query = common_query_builder(
        """{
            items { pValue }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minPValue": min_p_value,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["pValue"] >= min_p_value


def test_copyNumberResults_query_with_passed_min_p_value_and_min_log10_p_value(
    client, common_query_builder, test_cnr, min_log10_p_value, min_p_value
):
    query = common_query_builder(
        """{
            items { pValue }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minLog10PValue": min_log10_p_value,
                "minPValue": min_p_value,
                "tag": [test_cnr["tag"]],
                "paging": {"first": 10000},
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["pValue"] >= min_p_value


def test_copyNumberResults_query_with_passed_max_p_value(
    client, common_query_builder, test_cnr, max_p_value
):
    query = common_query_builder(
        """{
            items { pValue }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "maxPValue": max_p_value,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["pValue"] <= max_p_value


def test_copyNumberResults_query_with_passed_max_p_value_and_max_log10_p_value(
    client, common_query_builder, test_cnr, max_log10_p_value, max_p_value
):
    query = common_query_builder(
        """{
            items { pValue }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "maxLog10PValue": max_log10_p_value,
                "maxPValue": max_p_value,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["pValue"] <= max_p_value


def test_copyNumberResults_query_with_passed_min_log10_p_value(
    client, common_query_builder, test_cnr, min_log10_p_value
):
    query = common_query_builder(
        """{
            items { log10PValue }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minLog10PValue": min_log10_p_value,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["log10PValue"] >= min_log10_p_value


def test_copyNumberResults_query_with_passed_max_log10_p_value(
    client, common_query_builder, test_cnr, max_log10_p_value
):
    query = common_query_builder(
        """{
            items { log10PValue }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "maxLog10PValue": max_log10_p_value,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["log10PValue"] <= max_log10_p_value


def test_copyNumberResults_query_with_passed_min_mean_normal(
    client, common_query_builder, test_cnr, min_mean_normal
):
    query = common_query_builder(
        """{
            items { meanNormal }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minMeanNormal": min_mean_normal,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["meanNormal"] >= min_mean_normal


def test_copyNumberResults_query_with_passed_min_mean_cnv(
    client, common_query_builder, test_cnr, min_mean_cnv
):
    query = common_query_builder(
        """{
            items { meanCnv }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minMeanCnv": min_mean_cnv,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["meanCnv"] >= min_mean_cnv


def test_copyNumberResults_query_with_passed_min_t_stat(
    client, common_query_builder, test_cnr, min_t_stat
):
    query = common_query_builder(
        """{
            items { tStat }
        }"""
    )
    response = client.post(
        "/api",
        json={
            "query": query,
            "variables": {
                "dataSet": [test_cnr["dataset"]],
                "entrez": [test_cnr["entrez_id"]],
                "minTStat": min_t_stat,
                "tag": [test_cnr["tag"]],
            },
        },
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["tStat"] >= min_t_stat


def test_copyNumberResults_query_with_no_arguments(client, common_query_builder):
    query = common_query_builder(
        """{
            items {
                direction
                meanNormal
                meanCnv
                pValue
                log10PValue
                tStat
            }
        }"""
    )
    response = client.post(
        "/api", json={"query": query, "variables": {"paging": {"first": 10000}}}
    )
    json_data = json.loads(response.data)
    page = json_data["data"]["copyNumberResults"]
    results = page["items"]

    assert isinstance(results, list)
    assert len(results) > 0
    for result in results[0:2]:
        assert result["direction"] in direction_enum.enums
        assert type(result["meanNormal"]) is float or NoneType
        assert type(result["meanCnv"]) is float or NoneType
        assert type(result["pValue"]) is float or NoneType
        assert type(result["log10PValue"]) is float or NoneType
        assert type(result["tStat"]) is int or NoneType
