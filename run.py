from cadmus.cadmus import VagasCadmus
from excel.create_excel import CreateExcel
from cadmus.utilities import Utilities
import cadmus.constants as const
from mail.send_mail import SendMail

try:
    bot = VagasCadmus(const.CADMUS_URL)
    json_response = bot.get_body()
    if json_response:
        vacants_job = bot.list_values(json_response)
        excel = CreateExcel()
        excel.set_sheet_name()
        excel.set_headers()
        excel.write_lines(vacants_job)
        excel.save_excel()
        sm = SendMail(const.FROM_MAIL, const.PASS_MAIL, const.TO_MAIL, const.SUBJECT, const.BODY)
        sm.config_mail()
        sm.send_mail()
except BaseException as e:
    log = Utilities(e)
    log.register_log()