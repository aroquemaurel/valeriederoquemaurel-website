from valerie.common.models import Config


class ServicePhotos:
    _all_previous_photos = []
    _all_next_photos = []
    _current_photo = None
    _all_photos = []

    def __init__(self, all_photos):
        self._all_photos = all_photos

    def get_previous_photos(self, current_photo):
        if current_photo not in self._all_photos:
            return []

        self._init_all_photos_around(current_photo)

        if len(self._all_photos) <= (Config.NB_ELEMENTS_AROUND_PHOTO * 2 + 1):
            return self._all_previous_photos

        if len(self._all_previous_photos) > Config.NB_ELEMENTS_AROUND_PHOTO:
            return self._all_previous_photos[::-1][:Config.NB_ELEMENTS_AROUND_PHOTO][::-1]
        elif len(self._all_previous_photos) < Config.NB_ELEMENTS_AROUND_PHOTO:
            nb_next_photos_to_take = Config.NB_ELEMENTS_AROUND_PHOTO - len(self._all_previous_photos)
            return self._all_next_photos[::-1][:nb_next_photos_to_take][::-1] + self._all_previous_photos

        return self._all_previous_photos

    def get_next_photos(self, current_photo):
        if current_photo not in self._all_photos:
            return []

        self._init_all_photos_around(current_photo)

        if len(self._all_photos) <= (Config.NB_ELEMENTS_AROUND_PHOTO * 2 + 1):
            return self._all_next_photos

        if len(self._all_next_photos) > Config.NB_ELEMENTS_AROUND_PHOTO:
            return self._all_next_photos[:Config.NB_ELEMENTS_AROUND_PHOTO]
        elif len(self._all_next_photos) < Config.NB_ELEMENTS_AROUND_PHOTO:
            nb_previous_photos_to_take = Config.NB_ELEMENTS_AROUND_PHOTO - len(self._all_next_photos)
            return self._all_next_photos + self._all_previous_photos[:nb_previous_photos_to_take]

        return self._all_next_photos

    def _init_all_photos_around(self, current_photo):
        if self._current_photo == current_photo.id:
            return

        fill_previous = True
        self._all_previous_photos = []
        self._all_next_photos = []
        self._current_photo = current_photo
        for photo in self._all_photos:
            if photo == current_photo:
                fill_previous = False
            elif fill_previous:
                self._all_previous_photos.append(photo)
            else:
                self._all_next_photos.append(photo)