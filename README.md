# yuque_vercel_webhook_api
基于vercel的语雀severless云函数api部署

为了方便大家调用，我用 python 写了一个 api。
比较蛋疼的是，在仓库里填写 github 的私钥 github 会自动删除私钥。所以我试了好久都没成功。
因此，我直接将 api 设置成了参数传递型的，供大家调用。
api 地址：https://yuque-vercel-webhook-api.vercel.app/api?。
当然你也可以fork 项目在 vercel 中自行搭建，将 ‘https://yuque-vercel-webhook-api.vercel.app’ 更换为你的 app 应用链接。
你需要传递的参数有 token，user，source。

```
https://yuque-vercel-webhook-api.vercel.app/api?
token='{填写你的github私钥}'&
user='{填写你的github用户名}'&
source='{填写你的github仓库地址}'

示例：
https://yuque-vercel-webhook-api.vercel.app/api?token='8888888888'&user='Zfour'&source='my-blog-source-file'
将这个URL路径作为触发链接，在语雀中进行配置。
```

修改触发链接里的参数项，访问这个链接，如果出现‘This’s OK!’说明配置成功。
复制 URL 路径作为触发链接，在语雀中进行配置。
