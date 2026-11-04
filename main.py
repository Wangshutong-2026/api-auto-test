import pytest   #第二种方法
import os
pytest.main()

# 执行命令
os.system("allure generate -o report  -c temps")