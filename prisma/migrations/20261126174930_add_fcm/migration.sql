/*
  Warnings:

  - A unique constraint covering the columns `[fcm_token]` on the table `User` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `fcm_token` to the `User` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "User" ADD COLUMN     "fcm_token" TEXT NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "User_fcm_token_key" ON "User"("fcm_token");
