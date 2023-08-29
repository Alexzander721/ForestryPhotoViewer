# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ForestryPhotoViewer
                                 A QGIS plugin
 View photo fixation of the selection
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-30
        copyright            : (C) 2023 by Travin Alexzander/Roslesinforg
        email                : Alexzander721@mail.ru
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
    """Load ForestryPhotoViewer class from file ForestryPhotoViewer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .forestry_Photo_Viewer import ForestryPhotoViewer
    return ForestryPhotoViewer(iface)