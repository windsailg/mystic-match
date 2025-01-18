import { writeFile, mkdir } from 'fs/promises';
import { join } from 'path';
import { existsSync } from 'fs';
import { v4 as uuidv4 } from 'uuid';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const { image } = body;

  if (!image || !image.startsWith('data:image/png;base64,')) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Invalid or missing image data',
    });
  }

  const cookies = parseCookies(event);
  let userId = cookies.user_uuid;

  if (!userId) {
    userId = uuidv4();
    setCookie(event, 'user_uuid', userId, {
      httpOnly: true,
      path: '/',
      maxAge: 60 * 60 * 24 * 365,
    });
  }

  const base64Data = image.replace(/^data:image\/png;base64,/, '');
  const buffer = Buffer.from(base64Data, 'base64');

  const now = new Date();
  const dateFolder = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
  const userFolder = `${dateFolder}-${userId}`;
  const uploadDir = join(process.cwd(), 'public', 'uploads', userFolder);

  if (!existsSync(uploadDir)) {
    await mkdir(uploadDir, { recursive: true });
  }

  const fileName = `capture-${Date.now()}.jpg`;
  const filePath = join(uploadDir, fileName);
  await writeFile(filePath, buffer);

  return {
    message: 'Image uploaded successfully',
    path: `/uploads/${userFolder}/${fileName}`,
  };
});