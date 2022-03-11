P. Como escalar essa solução?

Resposta – Para escalar essa solução, abordaria dois caminhos:
1 - Pensar na arquitetura para execução da rotina. 
Penso que poderíamos seguir dois caminhos, usando em infraestrutura On Premise ou em algum provider de Cloud Computing. Para ambas as possibilidades, basicamente adotaria o Apache Spark, para usufruir de seus benefícios de processamento distribuído.
Solução que também proporia se caso adotasse Clou Computing. Logicamente respeitando os serviços de cada nuvem. Para a Azure, pensaria em HD Insight ou o Databricks, para utilização do Spark. Na AWS utilizaria o serviço EMR. E na GCP adotaria o Dataproc. 
2 – Necessidades além da substituição do Pandas
Essas possibilidades são pensando na substituição do Pandas pelo Spark, como maneira de se escalar a solução.
Também pode-se pensar na orquestração desse fluxo de trabalho. Para isso, penso que uma boa solução seria o Apache Airflow. Da mesma forma como o Apache Spark ele pode ser executado tanto em On Premise como em Cloud.
Caso haja necessidade de armazenar dados analíticos, pode-se pensar em soluções de armazenamento distribuído, como é o caso do HDFS, que também pode ser estruturado em infraestrutura On Premise quanto Cloud. Para isso temos o próprio cluster Hadoop, e suas respectivas soluções na nuvem. HD Insight, Azure Blob Storage e Azure Data Lake, na Azure. EMR e S3 na AWS. E Dataproc e Cloud Storage na GCP.
Ainda na compreensão de armazenamento distribuído, pode-se adotar formatos de arquivo específicos para computação distribuída como é o caso do Apache Parquet, Apache Avro, Apache ORC, Apache Avro, o próprio TXT; bem como as compressões GZIP e Snappy.
