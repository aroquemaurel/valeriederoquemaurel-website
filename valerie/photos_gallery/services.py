import logging
from itertools import chain

from valerie.common.models import Config
from valerie.photos_gallery.models import PhotoGallery

logger = logging.getLogger(__name__)


class ServiceGallery:
    _all_previous_photos = []
    _all_next_photos = []
    _current_photo = None
    _all_items = []

    def __init__(self, all_photos, all_videos):
        self._all_items = list(chain(all_photos, all_videos))
        self._all_items.sort(key=lambda x: x.position_Item)

    def get_previous_items(self, current_photo):
        if current_photo not in self._all_items:
            logger.warning("The item " + current_photo + " is not in the gallery.")
            return []

        self._init_all_photos_around(current_photo)
        nb_items = self._get_nb_items(current_photo)

        min_items = nb_items * 2 + 1
        if len(self._all_items) <= min:
            logger.debug("The number of items is lower or equal than " + min_items)
            return self._all_previous_photos

        if len(self._all_previous_photos) > nb_items:
            return self._all_previous_photos[::-1][:nb_items][::-1]
        elif len(self._all_previous_photos) < nb_items:
            nb_next_photos_to_take = nb_items - len(self._all_previous_photos)
            return self._all_next_photos[::-1][:nb_next_photos_to_take][::-1] + self._all_previous_photos

        return self._all_previous_photos

    def get_next_items(self, current_photo):
        if current_photo not in self._all_items:
            logger.warning("The item " + current_photo + " is not in the gallery.")
            return []

        self._init_all_photos_around(current_photo)
        nb_items = self._get_nb_items(current_photo)

        min_items = nb_items * 2 + 1
        if len(self._all_items) <= (nb_items * 2 + 1):
            logger.debug("The number of items is lower or equal than " + min_items)
            return self._all_next_photos

        if len(self._all_next_photos) > nb_items:
            return self._all_next_photos[:nb_items]
        elif len(self._all_next_photos) < nb_items:
            nb_previous_photos_to_take = nb_items - len(self._all_next_photos)
            return self._all_next_photos + self._all_previous_photos[:nb_previous_photos_to_take]

        return self._all_next_photos

    def _init_all_photos_around(self, current_photo):
        if self._current_photo == current_photo.id:
            return

        fill_previous = True
        self._all_previous_photos = []
        self._all_next_photos = []
        self._current_photo = current_photo
        for photo in self._all_items:
            if photo == current_photo:
                fill_previous = False
            elif fill_previous:
                self._all_previous_photos.append(photo)
            else:
                self._all_next_photos.append(photo)

    @staticmethod
    def _get_nb_items(current_photo):
        if isinstance(current_photo, PhotoGallery):
            return Config.NB_ELEMENTS_AROUND_PHOTO
        else:
            return Config.NB_ELEMENTS_AROUND_VIDEO
