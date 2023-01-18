Tutorial
=========

This tutorial guides you through how to work with Milvus and PyMilvus.

Prerequisites
-------------

Before we start, ensure that you have a PyMilvus distribution :ref:`installed<Installation>`. You can verify this by running the following in the Python shell without any prompted errors.

    >>> import pymilvus

This tutorial also assumes that a Milvus instance is running on :code:`localhost:19530`. To install Milvus, refer to `Install Milvus Standalone <https://milvus.io/docs/install_standalone-operator.md>`_ and `Install Milvus Cluster <https://milvus.io/docs/install_cluster-milvusoperator.md>`_ for details.

Connect to Your Milvus Database
-------------------------------

After you install a Milvus database, you can connect to it as follows:

   >>> import pymilvus
   >>> MILVUS_HOST_IP = 'localhost'
   >>> MILVUS_HOST_PORT = '19530'
   >>> try:
   ...     pymilvus.connect(MILVUS_HOST_IP, MILVUS_HOST_PORT)
   ...     print('Succeeded in connecting to Milvus.')
   ... except Exception:
   ...     print('Failed to connect to Milvus.')

If the connection succeeds, you should see the following message:

.. code-block:: shell

   Succeeded in connecting to Milvus.

If the connection fails, you should see the following message:

.. code-block:: shell

   Failed to connect to Milvus.   

Create a Schema
---------------

In a running Milvus instance, you can create multiple independent collections, each of which has its own data structure. In Milvus, we address the data structure of a collection **schema**, and data records in the collection **entities**.

You should create a schema before creating a collection and doing this is not a big deal:

    >>> pymilvus.create_schema()

Running the above snippet creates an empty schema, to which you can add some fields using the chainable method :doc:`pymilvus/CollectionSchema/add_field`. 

For each field, you should give it a name and a description, define its data type, and set other applicable attributes. Note that the attributes a field supports vary with its data type.

In this tutorial, we will use the following schema fields.

    >>> from pymilvus import DataType
    >>> schema = pymilvus.create_schema()
    ...           .add_field("id", DataType.INT64, is_primary=True, description="article id")
    ...           .add_field("title", DataType.VARCHAR, maxlength=512, description="article title")
    ...           .add_field("title_vector", DataType.FLOAT_VECTOR, dim=768, description="vector embeddings of title")
    ...           .add_field("link", DataType.STRING, max_length=512, description="url of the article")
    ...           .add_field("reading_time", DataType.INT64, description="reading time in minutes")
    ...           .add_field("publication", DataType.STRING, max_length=512, description="article category")
    ...           .add_field("claps", DataType.INT64, description="number of claps received")
    ...           .add_field("responses", DataType.INT64, description="number of comments received")

Create a Collection
-------------------

After the schema is ready, you can reference it while creating a collection:

    >>> import traceback
    >>> collection_name = 'medium_2020_dataset'
    >>> collection_desc = 'A set of articles published on Medium in 2020'
    >>> try:
    ...     pymilvus.create_collection(collection_name, schema, collection_desc)
    ...     print('Succeeded in creating collection %s' % collection_name)
    ... except Exception:
    ...     print('Oops! Something occured:\n %s' % traceback.print_exc())

If Milvus succeeds in creating this collection, you will see:

.. code-block::

    Succeeded in creating collection medium_2020_dataset.

Otherwise, you will see a traceback information instead.

Create an Index
---------------

All Approximate Nearest Neighbor (ANN) searches in Milvus rely on indexes for extremely high performance. Before any ANN searches, you have to create indexes on the vector field in your collection.

Now, we'll create an index for the vector field :code:`title_vector` in the collection just created.

    >>> index_params = {
    ...     "index_type": 'IVF_FLAT',
    ...     "metric_type": 'IP',
    ...     "params": { "nlist": 1024 }
    ... }
    >>> task = pymilvus.create_index('medium_2020_dataset', 'title_vector', 'title_vector_IF_IP', index_params)
    >>> task.wait()

In the above snippet, we have set :code:`index_type` to :code:`IVF_FLAT` and :code:`metric_type` to :code:`IP`. There are also other index types and metric types. For details, see `In-memory Index <https://milvus.io/docs/index.md>`_ and `On-disk Index <https://milvus.io/docs/disk_index.md>`_.

Running :doc:`pymilvus/create_index` lasts for a little while no matter what index type is in use. Just take a sip of coffee if it is by your hands and wait for the index to be created.

Till now, a brand new collection is ready for data input. Congrats!

Insert Some Entities
--------------------

In PyMilvus, you can either use :doc:`pymilvus/insert` to insert data records one after another or use :doc:`pymilvus/bulk_insert` to insert the whole dataset at a time.

Based on the schema created in a previous step, you can download the corresponding dataset `here <#>`_, which is a row-based JSON file.

Insert data records one by one
******************************

To insert data records one after another, you have to process the dataset for a little bit.

    >>> import pandas as pd
    >>> df = pd.read_json("medium_2020_dataset.json")
    >>> data = []
    >>> keys = df['rows'][0].keys()
    >>> for key in keys:
    >>>     data.append([ row.get(key) for row in df['rows'] ])
    >>> pymilvus.insert("medium_2020_dataset", data)

In the above snippet, we read the JSON file into memory and strip off the keys in each record to convert the dataset into a list of value lists. Then use :doc:`pymilvus/insert` to add the list into the collection.

Since the :doc:`pymilvus/insert` function uses a loop to insert the members of the input list and may be time-consuming if the list contains abundant high-dimensional members. You are advised to split your dataset into smaller chunks to prevent the insert process from lasting for a long time.

Insert the whole dataset at a time
**********************************

