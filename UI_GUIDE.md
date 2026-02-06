# UI Guide - Pravaah DL Causal Reasoning System

## 🎨 Modern Web Interface

The Pravaah DL Causal Reasoning System now features a stunning, modern web interface designed for optimal user experience.

## ✨ Key Features

### 1. **Beautiful Design**
- Gradient purple background with animated grid pattern
- Glassmorphism effects for panels
- Smooth animations and transitions
- Professional color scheme with indigo/purple accents

### 2. **Intuitive Layout**
- **Header Section**: Prominent branding with icon
- **Query Panel**: Full-width input area with all controls
- **Results Panel**: Detailed causal analysis display
- **History Panel**: Track all your queries

### 3. **Interactive Elements**
- Hover effects on all cards and buttons
- Animated loading spinner
- Real-time statistics dashboard
- Color-coded escalation badges

### 4. **Professional Icons**
- Font Awesome icons throughout
- Visual indicators for all sections
- Enhanced readability

## 🚀 Quick Start

### Starting the Application

```bash
# Method 1: Python
python app.py

# Method 2: Batch file (Windows)
start_webapp.bat
```

Then open your browser to: **http://localhost:5000**

## 📖 How to Use

### Step 1: Select Query Type
Choose between:
- **Single Query**: Start a new analysis
- **Follow-up Query**: Continue from previous context

### Step 2: Select Transcript (Optional)
- Choose a specific transcript ID
- Or leave as "All Transcripts" for broader analysis

### Step 3: Enter Your Query
Type your analytical question, such as:
- "Why do customers escalate complaints?"
- "What causes refund requests?"
- "Identify factors leading to long wait times"

### Step 4: Analyze
Click the **Analyze** button or press **Ctrl+Enter**

### Step 5: Review Results
The system displays:
- **Statistics**: Number of transcripts, calls, and evidence
- **Escalation Status**: Visual badge indicating escalation
- **Transcript IDs**: Relevant conversation identifiers
- **Call IDs**: Specific call references
- **Evidence**: Detailed conversation turns with relevance scores
- **Causal Factors**: Key factors with frequency counts

## 🎯 UI Components

### Query Input Panel
- **Query Type Selector**: Radio buttons with modern styling
- **Transcript Dropdown**: Select specific conversations
- **Text Area**: Large input field for queries
- **Action Buttons**: 
  - 🚀 Analyze (Primary action)
  - 🧹 Clear (Reset input)
  - 🔄 Reset Session (Clear history)

### Results Panel
- **Query Display**: Shows your question
- **Stats Grid**: 3-column metrics display
- **Escalation Badge**: Color-coded status indicator
- **Evidence Cards**: Expandable conversation details
- **Causal Factors**: Ranked list of contributing factors

### History Panel
- **Chronological List**: Most recent queries first
- **Quick Summary**: Call and evidence counts
- **Persistent Storage**: Maintains session history

## 🎨 Color Scheme

| Element | Color | Usage |
|---------|-------|-------|
| Primary | Indigo (#6366f1) | Main actions, headers |
| Secondary | Purple (#8b5cf6) | Accents, gradients |
| Success | Green (#10b981) | Positive indicators |
| Danger | Red (#ef4444) | Escalations, errors |
| Warning | Amber (#f59e0b) | Alerts |

## ⌨️ Keyboard Shortcuts

- **Ctrl + Enter**: Submit query
- **Tab**: Navigate between fields

## 📱 Responsive Design

The UI automatically adapts to:
- **Desktop**: Full 2-column layout
- **Tablet**: Stacked panels
- **Mobile**: Single column, optimized spacing

## 🔧 Customization

### Changing Colors
Edit the CSS variables in `templates/index.html`:

```css
:root {
    --primary: #6366f1;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    /* ... more variables */
}
```

### Modifying Layout
Adjust grid columns in `.main-content`:

```css
.main-content { 
    grid-template-columns: 1.2fr 0.8fr; 
}
```

## 🐛 Troubleshooting

### Issue: UI not loading
**Solution**: Ensure Flask is running and check console for errors

### Issue: Styles not applying
**Solution**: Clear browser cache (Ctrl+Shift+R)

### Issue: Icons not showing
**Solution**: Check internet connection (Font Awesome CDN required)

## 💡 Tips for Best Experience

1. **Use Chrome/Firefox**: Best compatibility
2. **Full Screen**: Maximize browser for optimal layout
3. **Clear History**: Reset session periodically for fresh start
4. **Specific Queries**: More detailed questions yield better results
5. **Follow-up Mode**: Use for contextual analysis

## 🎓 Example Queries

Try these sample queries:

```
1. "Why do customers request refunds?"
2. "What causes call escalations?"
3. "Identify patterns in customer complaints"
4. "Analyze factors leading to dissatisfaction"
5. "What triggers long wait times?"
```

## 📊 Understanding Results

### Relevance Score
- **90-100%**: Highly relevant
- **70-89%**: Moderately relevant
- **Below 70%**: Tangentially related

### Escalation Badge
- **Red (Escalated)**: Issue required escalation
- **Green (Not Escalated)**: Resolved normally

### Causal Factors
- Listed by frequency
- Higher numbers = more common cause

## 🚀 Performance

- **Average Query Time**: 2-5 seconds
- **Concurrent Users**: Supports multiple sessions
- **Cache**: Results cached for faster follow-ups

## 📞 Support

For issues or questions:
- Check console logs (F12 in browser)
- Review Flask terminal output
- Refer to main README.md

---

**Enjoy your enhanced causal reasoning experience!** 🎉
