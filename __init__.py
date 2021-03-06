# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ANADataAcquisition
                                 A QGIS plugin
 The ANA Data Acquisition tool automatically downloads several pluviometric and fluviometric stations provided by the brazilian National Water Agency (ANA)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-25
        copyright            : (C) 2020 by HGE-IPH
        email                : ingridp8396@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ANADataAcquisition class from file ANADataAcquisition.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ana_data_acquisition import ANADataAcquisition
    return ANADataAcquisition(iface)
