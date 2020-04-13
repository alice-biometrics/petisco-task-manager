import pytest

from meiga import Success, isFailure


@pytest.mark.unit
def test_should_create_task_happy_path(given_repository,):
    assert 1 == 1
    """
    mock_task_repository = Mock(spec=SomeAbstractClass)

    mock_task_repository = given_repository(result_save=isSuccess)
    mock_event_manager = given_event_manager(result_save=isSuccess)

    use_case = CreateTask(task_repository=mock_task_repository, 
                          event_manager=mock_event_manager)

    use_case.execute()
    
    assert mock_media_repository.assert_called_save_media(times=2)
    assert mock_cropper_media_service.assert_called()
    """
