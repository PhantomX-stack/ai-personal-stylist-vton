# Contributing to AI Personal Stylist

Thank you for your interest in contributing to AI Personal Stylist & Virtual Try-On! We welcome contributions of all kinds - whether it's bug fixes, new features, documentation improvements, or performance optimizations.

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## How to Get Started

### 1. Fork the Repository

```bash
git clone https://github.com/your-username/ai-personal-stylist-vton.git
cd ai-personal-stylist-vton
git remote add upstream https://github.com/PhantomX-stack/ai-personal-stylist-vton.git
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Adding or updating tests
- `perf/` - Performance improvements

### 3. Make Your Changes

- Keep commits atomic and focused
- Write clear, descriptive commit messages
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 4. Test Your Changes

**Backend Tests:**
```bash
cd backend
python -m pytest tests/
```

**Frontend Tests:**
```bash
cd frontend
npm test
```

**Manual Testing:**
- Test the application locally
- Verify both frontend and backend functionality
- Test edge cases and error scenarios

### 5. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the changes
- Detailed description of what was changed and why
- Reference to related issues (if any)
- Screenshots for UI changes

## Development Setup

### Backend Development

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r ../requirements.txt
uvicorn app:app --reload
```

### Frontend Development

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

## Project Structure

```
ai-personal-stylist-vton/
├── backend/
│   ├── app.py              # Main FastAPI application
│   ├── core/              # Core utilities
│   ├── services/          # Business logic
│   ├── vision/            # Computer vision modules
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/        # Page components
│   │   ├── services/     # API services
│   │   └── App.jsx       # Main app
│   ├── package.json      # Node dependencies
│   └── .env.example      # Environment template
└── README.md
```

## Coding Standards

### Python

- Follow PEP 8
- Use type hints for functions
- Write docstrings for modules and functions
- Use meaningful variable names

### JavaScript/React

- Use ES6+ features
- Follow React best practices
- Use functional components with hooks
- Add propTypes for component validation
- Keep components focused and reusable

## Commit Message Format

Use the following format for commit messages:

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Changes that don't affect code meaning
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `perf`: Performance improvements
- `chore`: Build process, dependencies, etc.

**Examples:**
```
feat: Add skin tone analysis API endpoint
fix: Resolve body type estimation accuracy issue
docs: Update installation guide for Windows users
```

## Pull Request Process

1. Update the README.md if needed
2. Update CHANGELOG.md with your changes
3. Ensure all tests pass
4. Ensure no conflicts with the main branch
5. Request reviews from maintainers
6. Address review feedback
7. Maintainers will merge when approved

## Reporting Bugs

When reporting bugs, please include:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Screenshots/videos if applicable
- System information (OS, Python version, Node version)
- Error messages and stack traces

## Feature Requests

When suggesting features, please include:

- Clear description of the feature
- Use cases and benefits
- Potential implementation approach
- Any relevant references or examples

## Performance Considerations

- API endpoints should respond in < 500ms
- Frontend should load in < 3s
- Vision analysis should complete in < 2s
- Use efficient algorithms for ML operations
- Minimize database queries
- Cache data when appropriate

## Documentation

- Keep README.md up to date
- Add docstrings to code
- Document complex algorithms
- Create issues for documentation improvements
- Update examples when behavior changes

## Questions?

- Check existing issues and discussions
- Review the README and documentation
- Ask in GitHub discussions
- Create an issue if you have suggestions

---

**Thank you for contributing to make AI Personal Stylist better! 🉋**
