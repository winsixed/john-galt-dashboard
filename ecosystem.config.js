module.exports = {
  apps: [
    {
      name: "backend",
      script: "uvicorn",
      args: "app.main:app --host 0.0.0.0 --port 8000",
      cwd: "./backend",
    },
    {
      name: "frontend",
      script: "pnpm",
      args: "start",
      cwd: "./frontend",
    },
    {
      name: "bot",
      script: "python",
      args: "app/bot/bot.py",
      cwd: "./backend",
    }
  ]
};
