import boto3

endpoint_url = "http://localhost.localstack.cloud:4566"


def main():
    client = boto3.client("lambda", endpoint_url=endpoint_url)
    result = client.list_functions()
    print(result)


if __name__ == "__main__":
    main()