export async function onRequest({ request, next }) {
  // 你自己设的后台密码，改成你想要的，比如 "sabaki123"
  const PASSWORD = "sabaki123";
  const url = new URL(request.url);
  const providedPassword = url.searchParams.get("password");

  // 如果密码不对，返回 401 未授权
  if (providedPassword !== PASSWORD) {
    return new Response(`
      <html>
        <head>
          <title>需要密码</title>
          <style>
            body { font-family: Arial; text-align: center; padding-top: 100px; background: #f5f5f5; }
            .box { background: white; padding: 30px; border-radius: 8px; display: inline-block; }
            input { padding: 10px; width: 200px; margin: 10px; }
            button { padding: 10px 20px; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }
          </style>
        </head>
        <body>
          <div class="box">
            <h2>🔒 售楼后台需要密码</h2>
            <form method="GET">
              <input type="password" name="password" placeholder="请输入密码" required>
              <br>
              <button type="submit">登录</button>
            </form>
          </div>
        </body>
      </html>
    `, {
      status: 401,
      headers: { "Content-Type": "text/html" }
    });
  }

  // 密码正确，正常访问页面
  return next();
}
