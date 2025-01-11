import { exec } from 'child_process';
import { resolve as resolvePath } from 'path';

const testJsonString = JSON.stringify({ fit: 1, style: 1, type: 1, color: 3 });

export default defineEventHandler(async (event) => {
  return new Promise((resolve, reject) => {
    // 使用绝对路径
    const scriptPath = resolvePath('server/scripts/python_src/run_python.sh');

    exec(`${scriptPath} '${testJsonString}'`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing script: ${error.message}`);
        reject({
          success: false,
          error: error.message,
        });
        return;
      }

      if (stderr) {
        console.error(`Script stderr: ${stderr}`);
      }

      console.log(`Script output: ${stdout}`);
      const output = JSON.parse(stdout);
      resolve({
        success: true,
        output: output,
      });
    });
  });
});
