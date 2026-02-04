# 🚀 Back Gate Guide - Setup Instructions

## Quick Overview
You'll get:
- ✅ A mobile-friendly page with directions
- ✅ Free hosting on GitHub Pages
- ✅ Free analytics via GoatCounter (page views, devices, locations)
- ✅ Optional: Detailed click tracking via Google Sheets

---

## STEP 1: Create GitHub Repository (5 minutes)

### 1.1 Go to GitHub
Open: https://github.com/new

### 1.2 Create Repository
- **Repository name:** `backgate-guide` (or any name you prefer)
- **Description:** Back entrance navigation for IT Park
- **Select:** ✅ Public
- **Select:** ✅ Add a README file
- Click **"Create repository"**

### 1.3 Upload the HTML File
1. In your new repository, click **"Add file"** → **"Upload files"**
2. Drag and drop the `index.html` file
3. Click **"Commit changes"**

### 1.4 Enable GitHub Pages
1. Go to repository **Settings** (tab at top)
2. Scroll down to **"Pages"** in left sidebar
3. Under "Source", select **"Deploy from a branch"**
4. Select branch: **main**, folder: **/ (root)**
5. Click **Save**
6. Wait 1-2 minutes, then your site will be live at:
   ```
   https://YOUR_USERNAME.github.io/backgate-guide/
   ```

---

## STEP 2: Set Up Free Analytics - GoatCounter (3 minutes)

GoatCounter is free, privacy-friendly, and shows you:
- Total page views
- Unique visitors
- Device types (Mobile/Desktop)
- Browsers
- Countries/Regions
- Which buttons people click

### 2.1 Sign Up
1. Go to: https://www.goatcounter.com/signup
2. Enter:
   - **Code:** `itpark-backgate` (this becomes your dashboard URL)
   - **Email:** Your email
   - **Password:** Choose one
3. Click **"Create"**

### 2.2 Add Tracking Code to Your Page
1. After signup, you'll get a code like: `itpark-backgate`
2. Open your `index.html` file in GitHub
3. Click the **pencil icon** to edit
4. Find this line (near the top):
   ```html
   <script data-goatcounter="https://YOUR_GOATCOUNTER_CODE.goatcounter.com/count"
   ```
5. Replace `YOUR_GOATCOUNTER_CODE` with your actual code (e.g., `itpark-backgate`)
6. Click **"Commit changes"**

### 2.3 View Your Dashboard
Go to: `https://YOUR_CODE.goatcounter.com`

Example: `https://itpark-backgate.goatcounter.com`

---

## STEP 3: Generate Your QR Code (2 minutes)

### Option A: Use Free Online Generator
1. Go to: https://www.qrcode-monkey.com/
2. Enter your GitHub Pages URL:
   ```
   https://YOUR_USERNAME.github.io/backgate-guide/
   ```
3. Customize colors (optional):
   - Body: #3b82f6 (blue)
   - Background: #ffffff (white)
4. Download PNG (high resolution)

### Option B: Use the QR Code I Generated
- Update the URL in the Python script provided and regenerate

---

## STEP 4 (Optional): Detailed Analytics with Google Sheets

For tracking EVERY click with full device details, set up Google Sheets logging:

### 4.1 Create Google Sheet
1. Go to: https://sheets.google.com
2. Create new spreadsheet named "BackGate Analytics"
3. Add headers in Row 1:
   ```
   Timestamp | Action | Device | OS | Browser | Screen | Language | Timezone
   ```

### 4.2 Create Google Apps Script
1. In your Sheet, go to **Extensions** → **Apps Script**
2. Delete default code and paste:

```javascript
function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = JSON.parse(e.postData.contents);
    
    sheet.appendRow([
      new Date().toISOString(),
      data.action || '',
      data.device || '',
      data.os || '',
      data.browser || '',
      (data.screenWidth || '') + 'x' + (data.screenHeight || ''),
      data.language || '',
      data.timezone || ''
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({status: 'success'}))
      .setMimeType(ContentService.MimeType.JSON);
  } catch(error) {
    return ContentService
      .createTextOutput(JSON.stringify({status: 'error', message: error.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

3. Click **Deploy** → **New deployment**
4. Select type: **Web app**
5. Set:
   - Execute as: **Me**
   - Who has access: **Anyone**
6. Click **Deploy** and copy the Web App URL

### 4.3 Add URL to Your HTML
1. Edit `index.html` on GitHub
2. Find this line:
   ```javascript
   GOOGLE_SCRIPT_URL: '',
   ```
3. Add your Web App URL:
   ```javascript
   GOOGLE_SCRIPT_URL: 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec',
   ```
4. Commit changes

Now every click logs to your Google Sheet with full device info! 📊

---

## 📍 Your Final URLs

After setup, you'll have:

| What | URL |
|------|-----|
| **QR Code Landing Page** | `https://YOUR_USERNAME.github.io/backgate-guide/` |
| **Analytics Dashboard** | `https://YOUR_CODE.goatcounter.com` |
| **Detailed Logs (optional)** | Your Google Sheet |

---

## 🔧 Need to Update Contacts or Locations?

1. Go to your GitHub repository
2. Click on `index.html`
3. Click the pencil icon to edit
4. Make changes
5. Click "Commit changes"
6. Changes go live in ~1 minute!

---

## 📱 Print the QR Code

For best results:
- Print at minimum 2cm x 2cm (0.8 inch)
- Use high contrast (dark QR on white background)
- Laminate for outdoor use
- Test scanning before mass distribution!

---

## Need Help?

Common issues:
- **Page not loading:** Wait 5 minutes after enabling GitHub Pages
- **Analytics not showing:** Check that GoatCounter code is correct
- **QR not scanning:** Make sure URL is exactly right, no typos

