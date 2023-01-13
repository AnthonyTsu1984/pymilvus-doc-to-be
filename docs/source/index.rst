.. PyMilvus documentation master file, created by
   sphinx-quickstart on Wed Jan 11 17:54:57 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyMilvus
========

Introduction
------------

Welcome to the documentation site for PyMilvus, the official Milvus SDK for python applications. Download it using `pip <https://pypi.org/project/pymilvus/>`_ or set up a runnable project by following our tutorial.


Compatibility
*************

.. list-table::
   :header-rows: 1
   :widths: 30 60

   * - Milvus Version
     - Recommended PyMilvus Version
   * - 1.0.x
     - 1.0.1
   * - 1.1.x
     - 1.1.2
   * - 2.0.x
     - 2.0.2
   * - 2.1.x
     - 2.1.3
   * - 2.2.x
     - 2.2.1 (latest)

Installation
------------

You must install the PyMilvus SDK to make it available for your Python applications. We recommend using `pip <https://pypi.org/project/pymilvus/>`_ to install PyMilvus.

The following command demonstrates how you can install the latest version of the module.

.. code-block:: shell

   python -m pip install pymilvus

To install a specific version of PyMilvus, do as follows:

.. code-block:: shell

   python -m pip install pymilvus=2.2.1

To upgrade your PyMilvus installation to the latest version, do as follows:

.. code-block:: shell

   python -m pip install --upgrade pymilvus


Let's enjoy!
------------

.. toctree::
   :maxdepth: 1

   tutorial
   pymilvus/index
   changelog
