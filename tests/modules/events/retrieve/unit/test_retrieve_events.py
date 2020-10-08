import pytest

from meiga import Success, isFailure
from unittest.mock import Mock

from meiga.assertions import assert_success, assert_failure
from petisco import IEventPublisher

from taskmanager.src.modules.events.application.retrieve.events_retriever import (
    EventsRetriever,
)
from taskmanager.src.modules.events.domain.interface_event_repository import (
    IEventRepository,
)


@pytest.mark.unit
def test_should_retrieve_events_happy_path(given_some_events):

    mock_event_repository = Mock(spec=IEventRepository)
    mock_event_repository.retrieve_all = Mock(return_value=Success(given_some_events))
    mock_event_publisher = Mock(spec=IEventPublisher)

    use_case = EventsRetriever(mock_event_repository, mock_event_publisher)

    result = use_case.execute()

    mock_event_repository.retrieve_all.assert_called_once()
    mock_event_publisher.publish.assert_called_once()

    assert_success(result)


def test_should_return_task_not_found_error():

    mock_event_repository = Mock(spec=IEventRepository)
    mock_event_repository.retrieve_all = Mock(return_value=isFailure)
    mock_event_publisher = Mock(spec=IEventPublisher)

    use_case = EventsRetriever(mock_event_repository, mock_event_publisher)

    result = use_case.execute()

    mock_event_repository.retrieve_all.assert_called_once()
    mock_event_publisher.publish.assert_not_called()

    assert_failure(result)
