import logging

import requests
from pdf2zh_next.config.model import SettingsModel
from pdf2zh_next.config.translate_engine_model import SungrowSettings
from pdf2zh_next.translator.base_rate_limiter import BaseRateLimiter
from pdf2zh_next.translator.base_translator import BaseTranslator
from tenacity import before_sleep_log
from tenacity import retry
from tenacity import retry_if_exception_type
from tenacity import stop_after_attempt
from tenacity import wait_exponential

logger = logging.getLogger(__name__)


class SungrowTranslator(BaseTranslator):
    """Sungrow公司翻译API实现类"""

    name = "sungrow"
    lang_map = {}

    def __init__(
        self,
        settings: SettingsModel,
        rate_limiter: BaseRateLimiter,
    ):
        super().__init__(settings, rate_limiter)

        # 获取 Sungrow 特定设置
        sungrow_settings: SungrowSettings = settings.translate_engine_settings

        self.api_url = sungrow_settings.sungrow_api_url
        self.username = sungrow_settings.sungrow_username
        self.password = sungrow_settings.sungrow_password
        self.tenant_id = sungrow_settings.sungrow_tenant_id
        self.scene = sungrow_settings.sungrow_scene
        self.timeout = (
            int(sungrow_settings.sungrow_timeout)
            if sungrow_settings.sungrow_timeout
            else 60
        )

        self.basic_auth = (self.username, self.password)

        # 验证设置
        sungrow_settings.validate_settings()

    @retry(
        retry=retry_if_exception_type(Exception),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=15),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )
    def do_translate(self, text: str, rate_limit_params: dict = None):
        """单文本翻译（符合BaseTranslator接口）"""
        if not text or not text.strip():
            return text

        payload = {
            "content": [text],
            "scene": self.scene,
            "inputLang": self.lang_in,
            "outputLang": self.lang_out,
        }
        headers = {"Content-Type": "application/json", "Tenant-Id": self.tenant_id}

        resp = requests.post(
            self.api_url,
            json=payload,
            headers=headers,
            auth=self.basic_auth,
            timeout=self.timeout,
        )
        resp.raise_for_status()

        data = resp.json()
        if data.get("code") == 0 and "data" in data:
            translate_res = data["data"].get("translateRes", [])
            return translate_res[0] if translate_res else text

        logger.warning(f"翻译API业务返回异常: {data}")
        return text
