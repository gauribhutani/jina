from jina.orchestrate.pods.container import ContainerPod
from jina.parsers import set_pod_parser


def test_container_pod_pass_envs():
    import docker

    with ContainerPod(
        set_pod_parser().parse_args(
            [
                '--uses',
                'docker://env-checker',
                '--env',
                'key1=value1',
                '--env',
                'key2=value2',
            ]
        )
    ) as pod:
        container = pod._container
        status = container.status

    assert status == 'running'
    client = docker.from_env()
    containers = client.containers.list()
    assert container.id not in containers
