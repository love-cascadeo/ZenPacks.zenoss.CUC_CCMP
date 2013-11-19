===============================
ZenPacks.zenoss.CUC_CCMP
===============================

.. contents::
    :depth: 3

About
-------

Provides basic monitoring of components in the Cisco Unified 
Communications Manager (formerly Cisco Unified CallManager and Cisco CallManager) solution.  

Limitations
-------------

Prerequisites
-------------------------------------------------------------------------------

==================  ==================================================================================
Prerequisite        Restriction
==================  ==================================================================================
Product             Zenoss 4.1.1 or higher
Required ZenPacks   None
Other dependencies  None
==================  ==================================================================================

Usage
-----

Installation
++++++++++++

Normal Installation (packaged egg)::

 $ zenpack --install ZenPacks.zenoss.CUC_CCMP-VERSION.egg
 $ zenwebserver restart

Developer Installation (link mode)::

 $ zenpack --link --install ZenPacks.zenoss.CUC_CCMP
 $ zenwebserver restart

Removal
+++++++


 $ zenpack --erase ZenPacks.zenoss.CUC_CCMP
 $ zenwebserver restart


Features
--------


Device Classes
++++++++++++++
A new device class located at **/Network/Cisco/CiscoCCMP** will be added

Device Template
+++++++++++++++
One new device templates will be added to the system. This template 
will be automatically bound to the device class **/Network/Cisco/CiscoCCMP**.

* CiscoCCMPDB

Component Templates
+++++++++++++++++++

No component template will be added.

Modeler Plugins
+++++++++++++++

No modeler plugin will be added.


zProperties
+++++++++++
No zProperties will be added.


Change Log
----------

* 1.0

  * Initial Release


Known Issues
------------

* No known issues