# pairwise-csrf-guard

后台管理站一加多标签页，CSRF 防护就漏：Origin 为空时直接放行，旧浏览器和隐私模式全部绕过；double-submit cookie 没有绑定会话，攻击者能自己种一个；token 在登录后不轮换，固定 token 可以跨账号复用；SameSite 只设 Lax，跨站 POST 仍会带 cookie；GET 请求能改状态，预检根本不触发。security/csrf_guard.py 是核心，tests/test_csrf_guard.py 15个红。要修的是：Origin/Referer 缺省拒绝；token 会话绑定；登录轮换；SameSite 策略；安全方法约束。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：漏洞检测与攻防；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
