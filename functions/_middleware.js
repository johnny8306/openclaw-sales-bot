export async function onRequest({ request, next }) {
  // 🔒 请在这里设置你的后台密码
  const PASSWORD = "sabaki123";
  const url = new URL(request.url);
  const providedPassword = url.searchParams.get("password");

  // 如果密码不对，返回登录页面
  if (providedPassword !== PASSWORD) {
    return new Response(`
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="UTF-8">
          <title>Access Restricted</title>
          <style>
            body { font-family: Arial; text-align: center; padding-top: 100px; background: #f5f5f5; }
            .box { background: white; padding: 30px; border-radius: 8px; display: inline-block; }
            input { padding: 10px; width: 200px; margin: 10px; }
            button { padding: 10px 20px; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }
          </style>
        </head>
        <body>
          <div class="box">
            <h2>🔒 Sales Backend Access Required</h2>
            <form method="GET">
              <input type="password" name="password" placeholder="Enter password" required>
              <br>
              <button type="submit">Login</button>
            </form>
          </div>
        </body>
      </html>
    `, {
      status: 401,
      headers: { "Content-Type": "text/html; charset=utf-8" }
    });
  }

  // 密码正确，正常访问页面
  return next();
}
