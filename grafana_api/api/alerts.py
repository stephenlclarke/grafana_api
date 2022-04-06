from .base import Base


class Alerts(Base):
    def __init__(self, api):
        super(Alerts, self).__init__(api)
        self.api = api

    def get_alerts(
        self,
        dashboard_ids=None,
        panel_ids=None,
        query=None,
        state=None,
        limit=None,
        folder_ids=None,
        dashboard_query=None,
        dashboard_tags=None,
    ):
        """

        :param dashboard_ids:
        :param panel_ids:
        :param query:
        :param state:
        :param limit:
        :param folder_ids:
        :param dashboard_query:
        :param dashboard_tags:
        :return:
        """
        get_alerts_path = "/alerts"
        params = []

        if dashboard_ids:
            params.append("dashboardIds=%s" % dashboard_ids)

        if panel_ids:
            params.append("panelId=%s" % panel_ids)

        if query:
            params.append("query=%s" % query)

        if state:
            params.append("state=%s" % state)

        if limit:
            params.append("limit=%s" % limit)

        if folder_ids:
            params.append("folderId=%s" % folder_ids)

        if dashboard_query:
            params.append("dashboardQuery=%s" % dashboard_query)

        if dashboard_tags:
            params.append("dashboardTag=%s" % dashboard_tags)

        get_alerts_path += "?"
        get_alerts_path += "&".join(params)

        r = self.api.GET(get_alerts_path)
        return r

    def get_alert_by_id(self, id):
        """

        :param id:
        :return:
        """
        get_alert_by_id_path = "/alerts/%s" % id
        r = self.api.GET(get_alert_by_id_path)
        return r

    def pause_alert_by_id(self, id):
        """

        :param id:
        :return:
        """
        pause_alert__path = "/alerts/%s/pause" % id
        r = self.api.POST(pause_alert__path)
        return r
