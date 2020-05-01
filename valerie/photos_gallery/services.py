from valerie.common.models import Config


class ServicePhotos:
    _all_previous_photos = []
    _all_next_photos = []
    _current_photo = None
    _all_photos = []

    def __init__(self, all_photos):
        self.all_photos = all_photos

    def _init_all_photos_around(self, current_photo):
        if self._current_photo is not None and self._current_photo.id == current_photo.id:
            return

        fill_previous = True
        self._all_previous_photos = []
        self._all_next_photos = []
        self.current_photo = current_photo
        for photo in self.all_photos:
            if photo.id == current_photo.id:
                fill_previous = False
            elif fill_previous:
                self._all_previous_photos.append(photo)
            else:
                self._all_next_photos.append(photo)

    def get_previous_photos(self, current_photo):
        self._init_all_photos_around(current_photo)

        if len(self._all_previous_photos) > Config.NB_ELEMENTS_AROUND_PHOTO:
            return self._all_previous_photos[::-1][:Config.NB_ELEMENTS_AROUND_PHOTO][::-1]
        elif len(self._all_previous_photos) < Config.NB_ELEMENTS_AROUND_PHOTO:
            return self._all_next_photos[::-1][:Config.NB_ELEMENTS_AROUND_PHOTO][::-1]

        return self._all_previous_photos

    def get_next_photos(self, current_photo):
        self._init_all_photos_around(current_photo)

        if len(self._all_next_photos) > Config.NB_ELEMENTS_AROUND_PHOTO:
            return self._all_next_photos[:Config.NB_ELEMENTS_AROUND_PHOTO]
        elif len(self._all_next_photos) < Config.NB_ELEMENTS_AROUND_PHOTO:
            return self._all_previous_photos[:Config.NB_ELEMENTS_AROUND_PHOTO]
        return self._all_next_photos
