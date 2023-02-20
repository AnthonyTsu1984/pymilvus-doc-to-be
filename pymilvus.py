from enum import Enum

# collection
def create_collection(name, schema, **kwargs):
    """
    Creates a collection with a pre-defined schema.

    :param name: Specifies the name of a collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type name: str
    :param schema: Specifies the schema of the collection.

        To prepare a schema, use :func:`create_schema` to create a :class:`CollectionSchema` object, and then use the chainable :meth:`CollectionSchema.add_field` to add fields.
    :type schema: :class:`CollectionSchema`
    :param num_shards: (Optional) Specifies the number of shards in the collection.

        Any incoming DML request is routed to a shard based on the hash value of the affected primary key.

        The number of shards should be no greater than 256. The value defaults to 2, indicating that two shards are to be created.
    :type num_shards: int
    :param consistency_level: (Optional) Specifies the consistency level of the collection.

        Consistency in a distributed database specifically refers to the property that ensures every node or replica has the same view of data when writing or reading data at a given time. For details, refer to `Consistency Level <https://milvus.io/docs/consistency.md#Consistency-levels>`_.

        The value defaults to :meth:`ConsistencyLevel.Bounded`.
    :type consistency_level: :class:`ConsistencyLevel`
    :param properties: (Optional) Specifies optional properties of the collection.

        .. list-table::
            :widths: 30 30 30
            :header-rows: 1

            * - Property
              - Description
              - Default Value
            * - :code:`collection.ttl.seconds`
              - Time-to-live (TTL) of a collection
              - :code:`0`, indicating that no such limit applies.

    :type properties: dict
    :param description: (Optional) Specifies the description of the collection.

        A description should be a string of 1 to 65535 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).

        The value defaults to an empty string.
    :type description: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`

    >>> import pymilvus
    >>> from pymilvus import DataType
    >>> 
    >>> schema = pymilvus.create_schema()
    ...           .add_field("id", DataType.INT64, is_primary=True, description="article id")
    ...           .add_field("title", DataType.VARCHAR, maxlength=512, description="article title")
    ...           .add_field("title_vector", DataType.FLOAT_VECTOR, dim=768, description="vector embeddings of title")
    ...           .add_field("link", DataType.STRING, max_length=512, description="url of the article")
    ...           .add_field("reading_time", DataType.INT64, description="reading time in minutes")
    ...           .add_field("publication", DataType.STRING, max_length=512, description="article category")
    ...           .add_field("claps", DataType.INT64, description="number of claps received")
    ...           .add_field("responses", DataType.INT64, description="number of comments received")
    ...
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.create_collection("medium_2020_dataset", schema, description="A sample collection")
    """
    pass

def create_schema():
    """
    Creates an empty :class:`CollectionSchema` object.

    :raises:
    :returns: An empty **CollectionSchema** object
    :rtype: :class:`CollectionSchema`

    >>> import pymilvus
    >>> from pymilvus import DataType
    >>> 
    >>> schema = pymilvus.create_schema()
    ...           .add_field("id", DataType.INT64, is_primary=True, description="article id")
    ...           .add_field("title", DataType.VARCHAR, maxlength=512, description="article title")
    ...           .add_field("title_vector", DataType.FLOAT_VECTOR, dim=768, description="vector embeddings of title")
    ...           .add_field("link", DataType.STRING, max_length=512, description="url of the article")
    ...           .add_field("reading_time", DataType.INT64, description="reading time in minutes")
    ...           .add_field("publication", DataType.STRING, max_length=512, description="article category")
    ...           .add_field("claps", DataType.INT64, description="number of claps received")
    ...           .add_field("responses", DataType.INT64, description="number of comments received")
    """
    pass

def describe_collection(name, **kwargs):
    """
    Describes the detail of a collection.

    :param name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: A :code:`CollectionInfo` object lists the collection details
    :rtypes: :code:`CollectionInfo`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> desc = pymilvus.describe_collection("medium_2020_dataset")
    >>> pymilvus.format_dict(desc)
    {
        'name': 'articles',
        'alias': None,
        'create_time': '2022-10-01 16:13:50'
        'description': 'articles from a medium dataset at Kaggle',
        'auto_id': False,
        'consistency_level': <ConsistencyLevel.Bounded: 2>,
        'field_names': ['id', 'title_vector', 'category', 'url', 'reading_time'],
        'num_replicas': 3,
        'resource_groups': ['hp_x1_0xdf21', 'hp_x1_0xdc1e', 'hp_x1_0x3f00'],
        'num_shards': 2,
        'num_partitions': 1,
    }
    """
    pass

def load_collection(name, **kwargs):
    """
    Loads a collection to make it prepared for searches and queries.

    :param name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type name: 
    :param num_replicas: (Optional) Specifies the number of replicas to load.

        The value is an integer no greater than xx and defaults to 1, indicating that only one replica is loaded.
    :type num_replicas: int
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: A collection-loading task
    :rtype: :class:`Task`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)  
    >>> task = pymilvus.load_collection("medium_2020_dataset")
    >>> task.wait()
    """
    pass

def release_collection(name, **kwargs):
    """
    Releases the loaded collection from memory. All data in the released collection remains intact after this operation. You can load the collection to memory again using :func:`load_collection`. 

    :param name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :return: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.load_collection("medium_2020_dataset")
    >>> pymilvus.release_collection("medium_2020_dataset") 
    """
    pass

def drop_collection(name, **kwargs):
    """
    Drops a collection with all the entities it contains.

    :param name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :return: No returns, indicating that this operation succeeds.
    :rtype: :class:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.drop_collection("medium_2020_dataset")     
    """
    pass

def get_collection_statistics(name, **kwargs):
    """
    Lists the statistical items of a collection.

    :param name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:    
    :returns: All statistical items of the collection
    :rtype: dict

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> desc = pymilvus.get_collection_statistics("medium_2020_dataset") 
    >>> pymilvus.form_dict(desc)
    {
        'row_count': 5979,
        'loaded_row_count': {
            'row': 5979,
            'titel_vector_ip': 5979,
            'category_tire': 5979,
            'reading_time_std': 5979,
        },
        'indexed_row_count': {
            'titel_vector_ip': 5979,
            'category_tire': 5979,
            'reading_time_std': 5979,
        },
    }       
    """
    pass

def list_collections(**kwargs):
    """
    Lists all collection names in the database.

    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:    
    :returns: A list of collection names
    :rtype: list[str]    

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.list_collections()
    ["medium_2020_dataset"]     
    """
    pass

def has_collection(name, **kwargs):
    """
    Shows whether a collection after the specified name exists.

    :param name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type name: str 
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :return: A boolean value indicating whether the collection exists.
    :rtype: bool

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.has_collection("medium_2020_dataset")
    True          
    """
    pass

# alias
def create_alias(alias, collection_name, **kwargs):
    """
    Creates an alias for a collection.

    :param alias: Specifies an alias desired for the collection.

        A collection alias should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type alias: str
    :param collection_name: Specifies the name of a target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.create_alias("medium_2020_dataset", "articles")
    """
    pass

def alter_alias(alias, collection_name, **kwargs):
    """
    Changes an alias for a collection.

    :param alias: Specifies an alias desired for the collection.

        A collection alias should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type alias: str
    :param collection_name: Specifies the name of a target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.alter_alias("medium_2020_dataset", "articles")    
    """
    pass

def list_aliases(collection_name, **kwargs):
    """
    Lists all aliases associated with the specified collection.

    :param collection_name: Specifies the name of a target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:    
    :returns: A list of aliases associated with a collection.
    :rtype: list[str]

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.list_aliases("medium_2020_dataset")
    ["articles", "passages"]       
    """
    pass

def drop_alias(alias, **kwargs):
    """
    Drops a specified alias.

    :param alias: Specifies an alias desired for the collection.

        A collection alias should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type alias: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.drop_alias("medium_2020_dataset", "articles")      
    """
    pass

def describe_alias(alias, **kwargs):
    """
    Describes a specified alias.

    :param alias: Specifies an alias desired for the collection.

        A collection alias should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type alias: str 
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: An :code:`AliasInfo` object lists the alias details
    :rtype: :code:`AliasInfo`   
    """
    pass

def has_alias(alias, **kwargs):
    """
    Checks whether the specified alias exists.

    :param alias: Specifies an alias desired for the collection.

        A collection alias should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type alias: str 
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: A boolean value indicating whether the specified alias exists
    :rtype: bool
    """ 
    pass

def create_index(collection_name, field_name, index_name, index_params, **kwargs):
    """
    Creates an index on the specified field in a collection.

    :param collection_name: Specifies a collection desired for the operation.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param field_name: Specifies the name of the field on which the index is to be created.

        A field name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).   
    :type field_name: str
    :param index_name: Specifies the name of the index for further reference.

        An index name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type index_name: str
    :param index_params: Specifies a set of index-tuning parameters.

        Index parameters comprise the index type, metric type, and other index-building / vector search parameters listed in the following table.

        .. list-table::
            :widths: 15 10 65
            :header-rows: 1

            * - Parameter
              - Type
              - Description
            * - :code:`index_type`
              - `str`
              - Specifies a valid indexing algorithm used to accelerate vector searches. For details, see `In-memory Index <https://milvus.io/docs/index.md>`_ and `On-disk Index <https://milvus.io/docs/disk_index.md>`_.
            * - :code:`metric_type`
              - `str`
              - Specifies a valid type of metrics used to measure vector similarities. For details, see `Similarity Metrics <https://milvus.io/docs/metric.md>`_.
            * - :code:`params`
              - `dict`
              - Specifies applicable index-building parameters. These parameters vary with index types. For details, see `In-memory Index <https://milvus.io/docs/index.md>`_ and `On-disk Index <https://milvus.io/docs/disk_index.md>`_.

    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: An index-creating task
    :rtype: :class:`Task` 

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> 
    >>> index_params = { 
    ...     "index_type": "IVF_FLAT",
    ...     "metric_type": "L2",
    ...     "params": { "nlist": 1024 }   
    ... }
    ... 
    >>> pymilvus.create_index("medium_2020_dataset", "title_vector", "title_vector_index", index_params)       
    """
    pass

def describe_index(collection_name, index_name, **kwargs):
    """
    Describes the index of a collection.

    :param collection_name: Specifies a collection desired for the collection.

        A collection collection should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param index_name: Specifies the name of the index for further reference.

        An index name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type index_name: str   
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: An :code:`IndexInfo` object lists the alias details
    :rtype: :code:`IndexInfo`  

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> desc = pymilvus.describe_index("medium_2020_dataset", "title_vector_index")
    >>> pymilvus.form_dict(desc)
    {
        'index_name': 'title_vector_ip',
        'field_name': 'title_vector',
        'index_type': 'AUTOINDEX',
        'metric_type': 'IP',
        'create_time': '2022-10-01 20:10:50',
    }          
    """
    pass

def drop_index(collection_name, index_name, **kwargs):
    """
    Drops the index of a collection.

    :param collection_name: Specifies a collection desired for the collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param index_name: Specifies the name of the index for further reference.

        An index name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type index_name: str   
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None

    :raises: 
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`  
    """
    pass

def has_index(collection_name, index_name, **kwargs):
    """
    Drops the index of a collection.

    :param collection_name: Specifies a collection desired for the collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param index_name: Specifies the name of the index for further reference.

        An index name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type index_name: str   
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None 

    :raises: 
    :returns: A boolean value indicating whether the specified index exists.
    :rtype: bool
    """    
    pass

def list_indexes(collection_name, field_name, **kwargs):
    """
    Lists the indexes built on the specified field.

    :param collection_name: Specifies a collection desired for the collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param field_name: Specifies the name of the field for further reference.

        An field name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type field_name: str   
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None 

    :raises: 
    :returns: A list of index names
    :rtype: list[str]
    """
    pass

def create_partition(collection_name, partition_name, **kwargs):
    """
    Creates a partition in a collection.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param partition_name: Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type partition_name: str  
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: No returns, indicating that this operation succeeds. 
    :rtype: :code:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.create_partition("medium_2020_dataset", "backup_partition")    
    """
    pass

def describe_partition(collection_name, partition_name, **kwargs):
    """
    Describes a partition of a collection.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param partition_name: Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type partition_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: A list of immutable attributes of the partition 
    :rtype: dict

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port) 
    >>> pymilvus.list_partitions("medium_2020_dataset")
    ["active_partition", "backup_partition"]
    >>> desc = pymilvus.describe_partition("medium_2020_dataset", "active_partition")
    {
        'name': '2020_Jan',
        'create_time': '2022-10-01 18:30:50',
        'description': 'articles published in Jan. 2020',
    }            
    """
    pass

def load_partition(collection_name, partition_names, **kwargs):
    """
    Loads only the specified partitions of a collection to memory.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str
    :param num_replicas: (Optional) Specifies the number of replicas to load.

        The value is an integer no greater than xx and defaults to 1, indicating that only one replica is loaded.
    :type num_replicas: int
    :param partition_name: Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type partition_name: list[str]  
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: A partition-loading task 
    :rtype: :class:`Task`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)  
    >>> task = pymilvus.load_partition("medium_2020_dataset", ["active_partition"])   
    >>> task.wait() 
    """
    pass

def release_partition(collection_name, partition_names, **kwargs):
    """
    Releases the specified partitions from memory. All data in the released partitions remain intact. You can load them into memory again using :func:`load_partition`.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param partition_name: Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type partition_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None 
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`  

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.load_collection("medium_2020_dataset")
    >>> pymilvus.release_collection("medium_2020_dataset")   
    """
    pass

def drop_partition(collection_name, partition_name, **kwargs):
    """
    Drops a partition and the data it contains from a collection.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param partition_name: Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type partition_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None 
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`  

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.drop_partition("medium_2020_dataset", "backup_partition")     
    """
    pass

def get_partition_statistics(collection_name, partition_names, **kwargs):
    """
    Lists all statistical items of specified partition names.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param partition_name: Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type partition_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises: 
    :return: All statistical items of the specified partitions.
    :rtype: dict

    >>> import pymilvus
    >>> pymilvus.list_partition('articles')
    ['2020_Jan', '2020_Feb', '2020_Mar', '2020_Apr', '2020_May', '2020_Jun', '2020_Jul', '2020_Aug', '2020_Sep', '2020_Oct', '2020_Nov', '2020_Sep']
    >>> desc = pymilvus.get_partition_statistics('articles', ['2020_Jan', '2020_Jul'])
    >>> pymilvus.format_dict(desc)     
    """
    pass

def list_partitions(collection_name, **kwargs):
    """
    Lists all partitions in a collection.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises: 
    :return: Names of all partitions in the collection
    :rtype: list[str]   

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.list_partitions("medium_2020_dataset")
    ["active_partition", "backup_partition"]        
    """
    pass

def has_partition(collection_name, partition_name, **kwargs):
    """
    Shows whether a partition after the specified name exists in a collection.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param partition_name: Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type partition_name: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: A boolean value indicating whether the partition exists.
    :rtype: bool

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.has_partition("medium_2020_dataset", "active_partition")
    True        
    """
    pass

def insert(collection_name, **kwargs):
    """
    Inserts a data record into the specified collection as an entity.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param data: Specifies the data record to be inserted.

        A data record is a list of valid scalar and vector values according to the schema. Given a schema defined as follows:

        .. code-block:: python

            import pymilvus

            schema = pymilvus.create_schema()
                .add_field("id", DataType.INT64, is_primary=True, description="article id")
                .add_field("title", DataType.VARCHAR, maxlength=512, description="article title")
                .add_field("title_vector", DataType.FLOAT_VECTOR, dim=768, description="vector embeddings of title")
                .add_field("link", DataType.STRING, max_length=512, description="url of the article")
                .add_field("reading_time", DataType.INT64, description="reading time in minutes")
                .add_field("publication", DataType.STRING, max_length=512, description="article category")
                .add_field("claps", DataType.INT64, description="number of claps received")
                .add_field("responses", DataType.INT64, description="number of comments received")

        An example data record should be

        * Either a list of tuples, each of which corresponds to a row in the dataset.   

        .. code-block:: python

            data = [
                (
                    0, 
                    "The Reported Mortality Rate of Coronavirus Is Not Important", 
                    [0.041732933, 0.013779674, -0.027564144, -0.013061441], 
                    "https://medium.com/swlh/the-reported-mortality-rate-of-coronavirus-is-not-important-369989c8d912", 
                    13, 
                    "The Startup", 
                    1100, 
                    18
                ),
                (
                    1,
                    "Dashboards in Python: 3 Advanced Examples for Dash Beginners and Everyone Else",
                    [0.0039737443, 0.003020432, -0.0006188639, 0.03913546], 
                    "https://medium.com/swlh/dashboards-in-python-3-advanced-examples-for-dash-beginners-and-everyone-else",
                    14,
                    "The Startup"
                    726,
                    3
                )  
            ]   

        * Or a list of lists, each of which corresponds to a field column.    

        .. code-block:: python

            data = [
                [
                    0,
                    1
                ],
                [
                    "The Reported Mortality Rate of Coronavirus Is Not Important",
                    "Dashboards in Python: 3 Advanced Examples for Dash Beginners and Everyone Else"
                ],
                [
                    [0.041732933, 0.013779674, -0.027564144, -0.013061441], 
                    [0.0039737443, 0.003020432, -0.0006188639, 0.03913546]
                ],
                [
                    "https://medium.com/swlh/the-reported-mortality-rate-of-coronavirus-is-not-important-369989c8d912", 
                    "https://medium.com/swlh/dashboards-in-python-3-advanced-examples-for-dash-beginners-and-everyone-else"
                ],
                [
                    13,
                    14
                ],
                [
                    "The Startup",
                    "The Startup"
                ],
                [
                    1100,
                    726
                ],
                [
                    18,
                    3
                ]
            ]                       
    :type data: list[any]
    :param partition_name: (Optional) Specifies the name of the target collection.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_). The default value is :code:`None`.
    :type partition_name: str or None  
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.insert("medium_2020_dataset", [
    ...     0, 
    ...     "The Reported Mortality Rate of Coronavirus Is Not Important", 
    ...     [0.041732933, 0.013779674, -0.027564144, -0.013061441], 
    ...     "https://medium.com/swlh/the-reported-mortality-rate-of-coronavirus-is-not-important-369989c8d912", 
    ...     13, 
    ...     "The Startup", 
    ...     1100, 
    ...     18      
    ... ])    
    """
    pass

def bulk_insert(collection_name, file, **kwargs):
    """
    Imports data from a specified file in an S3-like block storage system.

    :param collection_name: Specifies the name of the target collection.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param files: Specifies a list of file URLs.

        A valid file should be a row-based JSON file stored in an S3-like block storage system. Specifically, you need to organize your data in a dictionary with rows as the key and all the data records in a list as the value. In the list, each record corresponds to a dictionary. The key of each dictionary member is a field name, the values are those of these fields. Note that the file size should be no greater than 1 GB. 

        For your reference, the following is an example row-based JSON structure containing two entities.

        .. code-block:: python
            :caption: example_row-based.json

            {
                "rows": 
                [
                    {
                        "id": 0,
                        "title": "The Reported Mortality Rate of Coronavirus Is Not Important", 
                        "title_vector": [0.041732933, 0.013779674, -0.027564144, -0.013061441], 
                        "link": "https://medium.com/swlh/the-reported-mortality-rate-of-coronavirus-is-not-important-369989c8d912",
                        "reading_time": 13,
                        "publication": " The Startup",
                        "claps": 1100,
                        "responses": 18    
                    }, 
                    {
                        "id": 1,
                        "title": "Dashboards in Python: 3 Advanced Examples for Dash Beginners and Everyone Else", 
                        "title_vector": [0.0039737443, 0.003020432, -0.0006188639, 0.03913546], 
                        "link": "https://medium.com/swlh/dashboards-in-python-3-advanced-examples-for-dash-beginners-and-everyone-else",
                        "reading_time": 14,
                        "publication": " The Startup",
                        "claps": 726,
                        "responses": 3  
                    }
                ]
            }
    :type files: list[str] 
    :param partition_name: (Optional) Specifies the name of the target partition. If omitted, an arbitrary partition is selected.

        A partition name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_). The default value is :code:`None`.
    :type partition_name: str or None  
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :return: A handler of the bulk-insert task.
    :rtype: :class:`Task` 

    >>> import pymilvus
    >>> task = pymilvus.bulk_insert("medium_2020_dataset", "medium_2020_dataset.json")
    >>> task.wait()   
    """
    pass

def list_bulk_insert_tasks(**kwargs):
    """
    Lists all on-going bulk-insert tasks.

    :param limit: (Optional) Specifies the maximum number of tasks to be listed.

        The value defaults to 0, indicating that no such limit applies.
    :type limit: int or None
    :param collection_name: (Optional) Specifies the name of a collection so that only the tasks related to the collection are listed.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_). The value defaults to None, indicating no such limit applies.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type collection_name: str or None
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None 
    :raises:
    :returns: A list of bulk-insert task IDs.
    :rtype: list[str]

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> task = pymilvus.bulk_insert("medium_2020_dataset", "medium_2020_dataset.json")
    >>> pymilvus.list_bulk_insert_tasks()
    []        
    """
    pass

def get_bulk_insert_state(task_id, **kwargs):
    """
    Shows the state of a bulk-insert task.

    :param task_id: Specifies a task by its ID.

        You can get the ID of a task using :func:`list_bulk_insert_tasks()`
    :type task_id: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: State of the specified task.
    :rtype: dict

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> task = pymilvus.bulk_insert("medium_2020_dataset", "medium_2020_dataset.json")
    >>> pymilvus.list_bulk_insert_tasks()
    []
    >>> pymilvus.get_bulk_insert_state()
    """
    pass

def flush(collection_name, **kwargs):
    """
    Seals all entities in the specified collection. Any insertion after a flush operation results in generating new segments. Note that only sealed segments can be indexed.

    :param collection_name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None 
    :raises:
    :returns: No returns, indicating that this operation succeeds.
    :rtype: :code:`None`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.insert("medium_2020_dataset", [
    ...     0, 
    ...     "The Reported Mortality Rate of Coronavirus Is Not Important", 
    ...     [0.041732933, 0.013779674, -0.027564144, -0.013061441], 
    ...     "https://medium.com/swlh/the-reported-mortality-rate-of-coronavirus-is-not-important-369989c8d912", 
    ...     13, 
    ...     "The Startup", 
    ...     1100, 
    ...     18      
    ... ])
    >>> pymilvus.flush("medium_2020_dataset")
    """
    pass

def delete_by_expr(collection_name, **kwargs):
    """
    Deletes entities that match the specified expression from a collection.

    :param collection_name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param expr: Specifies a boolean expression to match desired entities.

        A valid boolean expression should comprise only the :code:`in` operator with two operands.
    :type expr: str
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: An entity-deleting task
    :rtype: :class:`Task`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.delete("medium_2020_dataset", "id in [1, 2, 3]")   
    """
    pass

def delete(collection_name, primary_keys, partition_names=None, **kwargs):
    """
    Deletes specified entities from a collection.

    :param collection_name: Specifies the name of the collection in concern.

        A collection name should be a string of 1 to 255 characters, starting with a letter or an underscore (_) and containing only numbers, letters, and underscores (_).
    :type collection_name: str 
    :param primary_keys: Specifies a list of entities in their primary keys.

        Including a non-existent primary key in the list may result in failures.
    :type primary_keys: list[int]
    :param timeout: (Optional) Specifies the timeout duration of this operation in seconds.

        The value defaults to :code:`None`, indicating that no such limit applies.
    :type timeout: float or None
    :raises:
    :returns: An entity-deleting task
    :rtype: :class:`Task`

    >>> import pymilvus
    >>> pymilvus.connect(ip_addr, port)
    >>> pymilvus.delete("medium_2020_dataset", [1, 2, 3])      
    """
    pass

class CollectionSchema:

    def add_field(name, data_type, **kwargs):
        """
        Adds a field to a schema.
        """
        pass


class Task:

    def wait():
        """
        A method used to wait for an asynchronous operation to complete
        """
        pass

    def get_progress():
        """
        A method used to get the progress of a task
        """
        pass

class ConsistencyLevel(Enum):
    """
    Enumerates all consistency levels of a collection. For details, see `Consistency Level <https://milvus.io/docs/consistency.md#Consistency-levels>`_.
    """
    STRONG = 1
    SESSION = 2
    BOUNDED = 3
    EVENTUALLY = 4

class DataType(Enum):
    """
    Enumerates all applicable data types in Milvus.
    """
    BOOL = 1
    INT8 = 2
    INT16 = 3
    INT32 = 4
    INT64 = 5
    FLOAT = 6
    DOUBLE = 7
    VARCHAR = 8
    BINARY_VECTOR = 9
    FLOAT_VECTOR = 10    
