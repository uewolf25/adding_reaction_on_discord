#!/.anyenv/envs/pyenv/shims/python
# -*- coding: utf-8 -*-

import os
import os.path
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

#　環境変数をセット
TOKEN = os.environ.get("TOKEN")
MY = os.environ.get("MY")
UN = os.environ.get("UN")
AUTHOR = os.environ.get("AUTHOR")
DEBUG_CH = os.environ.get("DEBUG_CH")

